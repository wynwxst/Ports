"""
 Implements a simple HTTP/1.0 Server

"""
from typing import Callable, Dict, Optional, Pattern, Set, Tuple
import re

import socket
import json

import io
import socket
import typing
from functools import partial

from collections import defaultdict













class Headers:
    """A mapping from lower-cased header names to lists of string values.
    """

    def __init__(self):
        self._headers = defaultdict(list)

    def add(self, name, value):
        self._headers[name.lower()].append(value)

    def get_all(self, name):
        return self._headers[name.lower()]

    def get(self, name, default=None):
        try:
            return self.get_all(name)[-1]
        except IndexError:
            return default

    def get_int(self, name):
        try:
            return int(self.get(name))
        except (TypeError, ValueError):
            return None

    def __iter__(self):
        for name, values in self._headers.items():
            for value in values:
                yield name, value



class BodyReader(io.IOBase):
    def __init__(self, sock: socket.socket, *, buff: bytes = b"", bufsize: int = 16_384) -> None:
        self._sock = sock
        self._buff = buff
        self._bufsize = bufsize

    def readable(self) -> bool:  # pragma: no cover
        return True

    def read(self, n: int) -> bytes:
        """Read up to n number of bytes from the request body.
        """
        while len(self._buff) < n:
            data = self._sock.recv(self._bufsize)
            if not data:
                break

            self._buff += data

        res, self._buff = self._buff[:n], self._buff[n:]
        return res


class Request(typing.NamedTuple):
    method: str
    path: str
    headers: Headers
    body: BodyReader

    @classmethod
    def from_socket(cls, sock: socket.socket) -> "Request":
        """Read and parse the request from a socket object.

        Raises:
          ValueError: When the request cannot be parsed.
        """
        lines = iter_lines(sock)

        try:
            request_line = next(lines).decode("ascii")
        except StopIteration:
            raise ValueError("Request line missing.")

        try:
            method, path, _ = request_line.split(" ")
        except ValueError:
            raise ValueError(f"Malformed request line {request_line!r}.")

        headers = Headers()
        buff = b""
        while True:
            try:
                line = next(lines)
            except StopIteration as e:
                buff = e.value
                break

            try:
                name, value = line.decode("ascii").split(":", 1)
                headers.add(name, value.lstrip())
            except ValueError:
                raise ValueError(f"Malformed header line {line!r}.")

        body = BodyReader(sock, buff=buff)
        return cls(method=method.upper(), path=path, headers=headers, body=body)


def iter_lines(sock: socket.socket, bufsize: int = 16_384) -> typing.Generator[bytes, None, bytes]:
    """Given a socket, read all the individual CRLF-separated lines
    and yield each one until an empty one is found.  Returns the
    remainder after the empty line.
    """
    buff = b""
    while True:
        data = sock.recv(bufsize)
        if not data:
            return b""

        buff += data
        while True:
            try:
                i = buff.index(b"\r\n")
                line, buff = buff[:i], buff[i + 2:]
                if not line:
                    return buff

                yield line
            except (IndexError, ValueError):
                break
import io
import os
import socket
import typing




class Response:
    """An HTTP response.

    Parameters:
      status: The response status line (eg. "200 OK").
      headers: The response headers.
      body: A file containing the response body.
      content: A string representing the response body.  If this is
        provided, then body is ignored.
      encoding: An encoding for the content, if provided.
    """

    status: bytes
    headers: Headers
    body: typing.IO[bytes]

    def __init__(
            self,
            status: str = "200 OK",
            headers: typing.Optional[Headers] = None,
            body: typing.Optional[typing.IO[bytes]] = None,
            content: typing.Optional[str] = None,
            encoding: str = "utf-8"
    ) -> None:

        self.status = status.encode()
        self.headers = headers or Headers()

        if content is not None:
            self.body = io.BytesIO(content.encode(encoding))
        elif body is None:
            self.body = io.BytesIO()
        else:
            self.body = body

    def send(self, sock: socket.socket) -> None:
        """Write this response to a socket.
        """
        content_length = self.headers.get_int("content-length")
        if content_length is None:
            try:
                body_stat = os.fstat(self.body.fileno())
                content_length = body_stat.st_size
            except OSError:
                self.body.seek(0, os.SEEK_END)
                content_length = self.body.tell()
                self.body.seek(0, os.SEEK_SET)

            if content_length > 0:
                self.headers.add("content-length", str(content_length))

        headers = b"HTTP/1.1 " + self.status + b"\r\n"
        for header_name, header_value in self.headers:
            headers += f"{header_name}: {header_value}\r\n".encode()

        sock.sendall(headers + b"\r\n")
        if content_length > 0:
            sock.sendfile(self.body)  # type: ignore

RouteHandlerT = Callable[..., Response]

HandlerT = Callable[[Request], Response]


class Core:
  def add_route(name: str, method: str, path: str,args, handler: RouteHandlerT) -> None:
          l = ""
          
          if name == None:
            name = path
          assert path.startswith("/"), "paths must start with '/'"
          if name in Ports.route_names:
              raise ValueError(f"A route named {name} already exists.")

          route_template = ""
          for segment in path.split("/")[1:]:
              if segment.startswith("{") and segment.endswith("}"):
                  segment_name = segment[1:-1]
                  #args.append(segment_name)
                  route_template += f"/(?P<{segment_name}>[^/]+)"
              else:
                  route_template += f"/{segment}"
                  l += f"/{segment}"


          route_re = re.compile(f"^{route_template}$")

          if l != "":
            name = l

          if name != "/" and name.endswith("/"):
          
            name = name[:-1]
          

          

          Ports.routes[method][name] = route_re, handler
          Ports.templates[method][name] = ""
          Ports.rargs[method][name] = args
          Ports.route_names.append(name)
          
        

  def lookup(method: str, path: str,args) -> Optional[HandlerT]:
      if args == None:
        args = {}
      if path in Ports.routes[method]:
          route_re, handler = Ports.routes[method][path]
          args = args
          x = partial(handler, **args)
          return x
      return None

import os
import json
import stat
import pathlib
import shutil
import sqlite3


class localStoragePyStorageException(Exception):
    pass


class BasicStorageBackend:
    def __init__(self, app_namespace: str) -> None:
        # self.base_storage_path = os.path.join(pathlib.Path.home() , ".config", "localStoragePy")
        if app_namespace.count(os.sep) > 0:
            raise localStoragePyStorageException('app_namespace may not contain path separators!')
        self.app_storage_path = os.path.join(pathlib.Path.home() , ".config", "localStoragePy", app_namespace)
        if not os.path.isdir(self.app_storage_path):
            os.makedirs(os.path.join(self.app_storage_path))

    def raise_dummy_exception(self):
        raise localStoragePyStorageException("Called dummy backend!")

    def get_item(self, item: str) -> str:
        self.raise_dummy_exception()

    def set_item(self, item: str, value: any) -> None:
        self.raise_dummy_exception()

    def remove_item(self, item: str) -> None:
        self.raise_dummy_exception()

    def clear(self) -> None:
        self.raise_dummy_exception()
        

class TextStorageBackend(BasicStorageBackend):
    def __init__(self, app_namespace: str) -> None:
        super().__init__(app_namespace)

    def shutil_error_path(self, func, path, exc_info):
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
        func(path)

    def get_file_path(self, key: str) -> os.PathLike:
        return os.path.join(self.app_storage_path, key)

    def get_item(self, key: str) -> str:
        item_path = self.get_file_path(key)
        if os.path.isfile(item_path):
            with open(item_path, "r") as item_file:
                return str(item_file.read())
        else:
            return None

    def set_item(self, key: str, value: any) -> None:
        item_path = self.get_file_path(key)
        with open(item_path, "w") as item_file:
            item_file.write(str(value))

    def remove_item(self, key: str) -> None: 
        item_path = self.get_file_path(key)
        if os.path.isfile(item_path):
            os.remove(item_path)

    def clear(self) -> None:
        if os.path.isdir(self.app_storage_path):
            shutil.rmtree(self.app_storage_path, onerror=self.shutil_error_path)
        os.makedirs(self.app_storage_path)


class SQLiteStorageBackend(BasicStorageBackend):
    def __init__(self, app_namespace: str) -> None:
        super().__init__(app_namespace)
        self.db_path = os.path.join(self.app_storage_path, "localStorageSQLite.db")
        self.db_connection = sqlite3.connect(self.db_path)
        self.db_cursor = self.db_connection.cursor()

        empty = self.db_cursor.execute("SELECT name FROM sqlite_master").fetchall()
        if empty == []:
            self.create_default_tables()

    def create_default_tables(self) -> None:
        self.db_cursor.execute("CREATE TABLE localStoragePy (key TEXT PRIMARY KEY, value TEXT)")
        self.db_connection.commit()
        
    def get_item(self, key: str) -> str:
        fetched_value = self.db_cursor.execute("SELECT value FROM localStoragePy WHERE key = ?", (key,)).fetchone()
        if type(fetched_value) is tuple:
            return fetched_value[0]
        else:
            return None

    def set_item(self, key: str, value: any) -> None:
        if len(self.db_cursor.execute("SELECT key FROM localStoragePy WHERE key = ?", (key,)).fetchall()) == 0:
            self.db_cursor.execute("INSERT INTO localStoragePy (key, value) VALUES (?, ?)", (key, str(value)))
        else:
            self.db_cursor.execute("UPDATE localStoragePy SET value = ? WHERE key = ?", (str(value), key))
        self.db_connection.commit()

    def remove_item(self, key: str) -> None:
        self.db_cursor.execute("DELETE FROM localStoragePy WHERE key = ?", (key,))
        self.db_connection.commit()

    def clear(self) -> None:
        self.db_cursor.execute("DROP TABLE localStoragePy")
        self.create_default_tables()


class JSONStorageBackend(BasicStorageBackend):
    def __init__(self, app_namespace: str) -> None:
        super().__init__(app_namespace)
        self.json_path = os.path.join(self.app_storage_path, "localStorageJSON.json")
        self.json_data = {}

        if not os.path.isfile(self.json_path):
            self.commit_to_disk()

        with open(self.json_path, "r") as json_file:
            self.json_data = json.load(json_file)
        
    def commit_to_disk(self):
        with open(self.json_path, "w") as json_file:
            json.dump(self.json_data, json_file)

    def get_item(self, key: str) -> str:
        if key in self.json_data:
            return self.json_data[key]
        return None

    def set_item(self, key: str, value: any) -> None:
        self.json_data[key] = str(value)
        self.commit_to_disk()

    def remove_item(self, key: str) -> None: 
        self.json_data.pop(key)
        self.commit_to_disk()

    def clear(self) -> None:
        if os.path.isfile(self.json_path):
            os.remove(self.json_path)
        self.json_data = {}
        self.commit_to_disk()
    
class localStorage:
    def __init__(self, app_namespace: str, storage_backend: str = "json") -> None:
        self.storage_backend_instance = BasicStorageBackend(app_namespace)
        if storage_backend == "text":
            self.storage_backend_instance = TextStorageBackend(app_namespace)
        elif storage_backend == "sqlite":
            self.storage_backend_instance = SQLiteStorageBackend(app_namespace)
        elif storage_backend == "json":
            self.storage_backend_instance = JSONStorageBackend(app_namespace)
        else:
            self.storage_backend_instance = SQLiteStorageBackend(app_namespace)

    def getItem(self, item: str) -> any:
        return self.storage_backend_instance.get_item(item)

    def setItem(self, item: str, value: any) -> None:
        self.storage_backend_instance.set_item(item, value)

    def removeItem(self, item: str) -> None:
        self.storage_backend_instance.remove_item(item)

    def clear(self):
        self.storage_backend_instance.clear()

    

class tools:
  def render_template(template,method="GET"):
    fin = open('templates/' + template)
    content = fin.read()
    fin.close()

    response = content
    return response

class Ports:

  #Databases

  env = {}
  config = {}
  routes = {"GET":{},"POST":{}}
  route_names = []
  templates = {"GET":{},"POST":{}}
  rargs = {"GET":{},"POST":{}}
  db = {}


  




  
  def route(
          path: str,
          args = [],
          method: str = "GET",
          name: Optional[str] = None,
  ) -> Callable[[RouteHandlerT], RouteHandlerT]:
      
      def decorator(handler: RouteHandlerT) -> RouteHandlerT:

          Core.add_route(name,method, path, args, handler)
          return handler
      return decorator

  def __call__(method,path,args) -> Response:
      handler = None
      if args == []:
        handler = Core.lookup(method, path,None)
      else:
        handler = "frenchbabyseal"

      e = Ports.rargs[method][path] == []
        

      

      if handler is None:
          print("No handler")
          return "HTTP/1.0 404 NOT FOUND\n\nRoute Not Found"
      if e == True:
        return handler()
      else:
        dargs = {}
        for arg in Ports.rargs[method][path]:
          if len(args) == 1:
            for item in args:
              l = item.split("=")
              dargs[l[0]] = l[1]
          else:
            lis = "".join(args)
            lis.split("&")
            for item in lis:
              l = item.split("=")
              dargs[l[0]] = l[1]
        handler = Core.lookup(method, path,dargs)




        return handler()




  



  def handle_request(request):
      args = None
      """Handles the HTTP request."""

      headers = request.split('\n')
      
      filename = headers[0].split()[1]
      print(headers[0])
      method = headers[0].split()
      method = method[0]
      if "?" in filename:
        args = filename.split("?")
        filename = args[0]
        args = [args[1]]
        
      else:
        args = []
      if filename.endswith("/") and filename != "/":
        filename = filename[:-1]
        args = []

        # keyerror cuz doesn't become just /hello


      if Ports.config["static"]:
        try:
          if filename == "/":
            filename = "index.html"
          fin = open('www/' + filename)
          content = fin.read()
          fin.close()
          response = 'HTTP/1.0 200 OK\n\n' + content
        except FileNotFoundError:
          response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

        
      else:

        print(f"PATH:'{filename}' | ARGS:'{args}'")
        if filename not in Ports.routes[method]:
          print("NonExistent")
          response = 'HTTP/1.0 404 NOT FOUND\n\nRoute Not Found'
        else:


          try:
            if Ports.templates[method][filename] != "":
              fin = open('templates/' + Ports.templates[method][filename])
              content = fin.read()
              fin.close()

              response = 'HTTP/1.0 200 OK\n\n' + content
            else:
              try:
                
                response = Ports.__call__(method,filename,args)
                response = "HTTP/1.0 200 OK\n\n" + response
              except Exception as e:
                response = Response(status="500 Internal Server Error", content="Internal Error")
          except FileNotFoundError:
              print("FNF")
              response = 'HTTP/1.0 404 NOT FOUND\n\nRoute Not Found'

      return response



  def run(SERVER_HOST,SERVER_PORT):
    Ports.config["host"] = SERVER_HOST
    Ports.config["port"] = SERVER_PORT

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)

    while True:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()

        # Return an HTTP response
        response = Ports.handle_request(request)
        client_connection.sendall(response.encode())

        # Close connection
        client_connection.close()

    # Close socket
    server_socket.close()



def app(name=""):
  Ports.config["name"] = name
  Ports.config["static"] = False
  return Ports

def static_app(name=""):
  Ports.config["name"] = name
  Ports.config["static"] = True
  return Ports