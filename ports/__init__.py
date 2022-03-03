
from typing import Callable, Dict, Optional, Pattern, Set, Tuple, List, Union
import re
import socket
import requests
import json
import io
import typing
from functools import partial
import random
from collections import defaultdict
import os
import stat
import pathlib
import shutil
import sqlite3
import logging
from queue import Empty, Queue
from threading import Thread
import sys
import functools
import mimetypes
from datetime import datetime

def loadModule(moduleName):
    module = None
    try:
        import sys
        del sys.modules[moduleName]
    except BaseException as err:
        pass
    try:
        import importlib
        module = importlib.import_module(moduleName)
    except BaseException as err:
        serr = str(err)
        print("Error to load the module '" + moduleName + "': " + serr)
    return module

def reloadModule(moduleName):
    module = loadModule(moduleName)
    moduleName, modulePath = str(module).replace("' from '", "||").replace("<module '", '').replace("'>", '').split("||")
    if (modulePath.endswith(".pyc")):
        import os
        os.remove(modulePath)
        module = loadModule(moduleName)
    return module

def getInstance(moduleName, param1, param2, param3):
    module = reloadModule(moduleName)
    instance = eval("module." + moduleName + "(param1, param2, param3)")
    return instance

FILE_RESPONSE_TEMPLATE = """\
HTTP/1.1 200 OK
Content-type: {content_type}
Content-length: {content_length}

""".replace("\n", "\r\n")






def getlocalhost():
  plat = sys.platform
  print(f"Launching on {plat}...")
  if plat.startswith("win"):
    plat = "127.0.0.1"
  else:
    plat = "0.0.0.0"
  return plat


      


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
    h = []
    stat = None

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
        if Response.stat == None:
          self.status = status.encode()
        else:
          self.status = Response.stat.encode()

        if Ports.sendrn == False:

          if content is not None:
              self.body = io.BytesIO(content.encode(encoding))
          elif body is None:
              self.body = io.BytesIO()
          else:
              self.body = body
        else:
          self.content = content


          #self.content = bytes(content.encode(encoding))

    def send(self, sock: socket.socket) -> None:
        """Write this response to a socket.
        """
        if Ports.sendrn == False:

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
          for head in Ports.headers:
            headers += f"{head}\r\n".encode()

          sock.sendall(headers + b"\r\n")
          if content_length > 0:
              sock.sendfile(self.body) 
           # type: ignore
        else:
          ok = "frenchbabyseal"

          #add_file("indra.jpg",sock,"indra.jpg")

RouteHandlerT = Callable[..., Response]

HandlerT = Callable[[Request], Response]


class Core:
  def add_route(name: str, methods: str, path: str,args, handler: RouteHandlerT) -> None:
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

          for method in methods:
            if method not in Ports.rargs and Ports.routes and Ports.templates:
              Ports.rargs[method] = {}
              Ports.templates[method] = {}
              Ports.routes[method] = {}





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
  def add_file(path,sock,aath=None):
    path = f"{path}"
    try:
      with open(path, "rb") as f:
        stat = os.fstat(f.fileno())
        content_type, encoding = mimetypes.guess_type(path)
        if content_type is None:
            content_type = "application/octet-stream"
      
        if encoding is not None:
            content_type += f"; charset={encoding}"
      
        response_headers = FILE_RESPONSE_TEMPLATE.format(
            content_type=content_type,
            content_length=stat.st_size,
        ).encode("ascii")
      
        sock.sendall(response_headers)
        sock.sendfile(f)
    except:
      return "ERROR"
  def get_addr():
    return str(Ports.client["ip"])
  def get_hostname():
    return str(Ports.client["name"])
  def send_file(file):
    Ports.sendrn = True
    x = tools.add_file(file,Ports.sock)
    return x
    

  def render_template(template,vars={}):
    fin = open('templates/' + template)
    content = fin.read()
    amt = 0
    finder = open('templates/' + template)
    lines = finder.readlines()
    lvars = {}
    found = False
    func = ""
    for line in lines:
      line = line.replace("\n","")
      

      amt += 1
      locl = {}
      fund = False
      if found == True:
        if line.startswith("|\|"):
          exec(func,{},locl)
          lvars[str(amt)] = locl
          func = ""
          fund = True
          
        else:
          content = content.replace(f"{line}\n","")
          func += line
      if line != "\n" and found == False:
        
        if line.startswith("|\|"):
          found = True
          fund = False
      if fund == True:
        found = False
    for item in vars:
      content = content.replace(f"[[{item}]]",str(vars[item]))

    for itee in lvars:
      for var in lvars[itee]:
        content = content.replace(f"[[{var}]]",str(lvars[itee][var]))
    content = content.replace("|\|\n","")



      

    fin.close()

    response = content
    return response
  def jsonify(content):

      return str(content)


class Ports:

  #Databases
  sock = ""
  env = {}
  config = {}
  routes = {"GET":{},"POST":{}}
  route_names = []
  templates = {"GET":{},"POST":{}}
  rargs = {"GET":{},"POST":{}}
  db = {}
  cookies = {}
  path = ""
  method = ""
  headers = []
  client = {}
  heads = ""
  location = ""
  cookiejar = ""
  Request = ""
  Headers = ""
  sendrn = False




  class Cookies:
    
    def set(name,value,expiry=None):
      x = ""
      if expiry == None:
        x = f"Set-Cookie: {name}={value}"
      else:
        now = datetime.now()
        exp = now + datetime.timedelta(seconds = expiry)
        x = f"Set-Cookie: {name}={value}; Expires={exp}; Path={Ports.path}"
      Ports.headers.append(x)
      
      

    def delete(name):
      exp = "Thu, 01 Jan 1970 00:00:00 GMT;"
      value = "deleted"
      x = ""



      x = f"Set-Cookie: {name}={value}; expires={exp}; Path={Ports.path}"

      Ports.headers.append(x)
    def get_all():
      cookiez = {}
      cookiejar = Ports.cookiejar
      cookiejar = "".join(cookiejar)
      cookiejar = cookiejar.split("; ")

      

      for cookie in cookiejar:
        if cookiejar == [''] or cookiejar == []:
          return "No Cookies stored"
        
        cks = cookie.split("=")
        name = cks[0]
        value = cks[1]
        cookiez[name] = value
      return cookiez
    def get(namer):
      cookiez = {}

      cookiejar = Ports.cookiejar
      cookiejar = "".join(cookiejar)
      cookiejar = cookiejar.split("; ")


      for cookie in cookiejar:
        if cookiejar == [''] or cookiejar == []:
          return "No Cookies stored"
        
        cks = cookie.split("=")
        name = cks[0]
        value = cks[1]
        cookiez[name] = value
      if namer not in cookiez:
        return "Cookie not found"
      return str(cookiez[namer])





  def route(
          path: str,
          args = [],
          methods = ["GET"],
          name: Optional[str] = None,
  ) -> Callable[[RouteHandlerT], RouteHandlerT]:

      def decorator(handler: RouteHandlerT) -> RouteHandlerT:

          Core.add_route(name,methods, path, args, handler)
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
          return "Route Not Found"
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
      filename = request.path
      method = request.method
      args = None
      """Handles the HTTP request."""
      timern = datetime.now()

      print(f"{request.method} {request.path} at {timern}")
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
          response = '' + content
        except FileNotFoundError:
          response = 'File Not Found'


      else:
        if filename.startswith("/static/"):
          tose = filename.replace("/static/","static/")
          return tools.send_file(f"{tose}")

        print(f"PATH:'{filename}' | ARGS:'{args}'")
        if filename not in Ports.routes[method]:
          print("NonExistent")
          response = 'Route Not Found'
        else:


          try:
            if Ports.templates[method][filename] != "":
              fin = open('templates/' + Ports.templates[method][filename])
              content = fin.read()
              fin.close()

              response = '' + content
            else:
              try:

                response = Ports.__call__(method,filename,args)
                response = "" + response
              except Exception as e:
                print(e)
                response = Response(status="500 Internal Server Error", content="Internal Error")
          except FileNotFoundError:
              print("FNF")
              response = 'Route Not Found'

      return response



  def run(host=getlocalhost(), port=random.randint(1000,9000), worker_count=16) -> int:
    if "host" in Ports.config:
      host = Ports.config["host"]
    if "port" in Ports.config:
      port = Ports.config["port"]
    for ext in globals.extensions:
      with open(ext) as x:
        content = x.read()
        exec(f"{content}\nsetup(appkey)",{"appkey":globals.app})

    Ports.config["host"] = host
    Ports.config["port"] = port
    server = HTTPServer(host,port,worker_count)
    server.mount("", APP)
    server.serve_forever()
    return 0

LOGGER = logging.getLogger(__name__)

class HTTPWorker(Thread):
    def __init__(self, connection_queue: Queue, handlers: List[Tuple[str, HandlerT]]) -> None:
        super().__init__(daemon=True)

        self.connection_queue = connection_queue
        self.handlers = handlers
        self.running = False

    def stop(self) -> None:
        self.running = False
    def getsock(self) -> None:
      while self.running:
            try:
                client_sock, client_addr = self.connection_queue.get(timeout=1)
                return client_sock, client_addr
            except Empty:
                continue
    def run(self) -> None:
        self.running = True
        while self.running:
            try:
                client_sock, client_addr = self.connection_queue.get(timeout=1)
            except Empty:
                continue

            try:
                self.handle_client(client_sock, client_addr)
            except Exception:
                LOGGER.exception("Unhandled error in handle_client.")
                continue
            finally:
                self.connection_queue.task_done()

    def handle_client(self, client_sock: socket.socket, client_addr: typing.Tuple[str, int]) -> None:
        with client_sock:
            try:
                request = Request.from_socket(client_sock)
            except Exception:
                LOGGER.warning("Failed to parse request.", exc_info=True)
                response = Response(status="400 Bad Request", content="Bad Request")
                response.send(client_sock)
                return

            # Force clients to send their request bodies on every
            # request rather than making the handlers deal with this.
            if "100-continue" in request.headers.get("expect", ""):
                response = Response(status="100 Continue")
                response.send(client_sock)

            for path_prefix, handler in self.handlers:
                if request.path.startswith(path_prefix):
                    try:
                        request = request._replace(path=request.path[len(path_prefix):])
                        Ports.Request = request
                        Ports.sock = client_sock
                        Ports.sendrn = False
                        Ports.path = request.path
                        Ports.method = request.method
                        Ports.Headers = request.headers
                        Ports.location = request.headers.get("host")
                        Ports.cookiejar = request.headers.get_all("cookie")
                        Ports.heads = request.headers._headers
                        Ports.client["name"] = socket.gethostname()
                        Ports.client["ip"] = request.headers.get("x-forwarded-for")
                        response = Ports.handle_request(request)
                        response = Response(status="200 OK",content=response)
                        response.send(client_sock)
                    except Exception as e:
                        LOGGER.exception("Unexpected error from handler %r.", handler)
                        response = Response(status="500 Internal Server Error", content="Internal Error")
                        response.send(client_sock)
                    finally:
                        break
            else:
                response = Response(status="404 Not Found", content="Not Found")
                response.send(client_sock)


class HTTPServer:
    def __init__(self, host="0.0.0.0", port=9000, worker_count=16) -> None:
        self.handlers: List[Tuple[str, HandlerT]] = []
        self.host = host
        self.port = port
        self.worker_count = worker_count
        self.worker_backlog = worker_count * 8
        self.connection_queue: Queue = Queue(self.worker_backlog)

    def mount(self, path_prefix: str, handler: HandlerT) -> None:
        """Mount a request handler at a particular path.  Handler
        prefixes are tested in the order that they are added so the
        first match "wins".
        """

        self.handlers.append((path_prefix, handler))

    def serve_forever(self) -> None:
        workers = []
        for _ in range(self.worker_count):
            worker = HTTPWorker(self.connection_queue, self.handlers)
            worker.start()
            workers.append(worker)

        with socket.socket() as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind((self.host, self.port))
            server_sock.listen(self.worker_backlog)
            LOGGER.info("Listening on %s:%d...", self.host, self.port)
            print(f"Listening on {self.host}:{self.port}...")

            while True:
                try:
                    self.connection_queue.put(server_sock.accept())
                except KeyboardInterrupt:
                    server_sock.close()
                    worker.stop()
                    break

        for worker in workers:
            worker.stop()

        for worker in workers:
            worker.join(timeout=30)


class managers:

  class extensions:

    def register(plugin):
      globals.extensions.append(plugin)
    def regall(dir):
      for file in os.listdir(dir):
        globals.extensions.append(file)

    
    
    
class globals:
  extensions = []
  app = ""

def APP(name=__name__):
  print(f"starting {name}!")
  Ports.config["name"] = name
  Ports.config["static"] = False
  globals.app = Ports
  return globals.app

def static_APP(name=__name__,path=""):
  print(f"starting {name}!")
  Ports.config["name"] = name

  Ports.config["static"] = True
  globals.app = Ports
  return globals.app

try:
  if sys.argv[1] == "run":
    os.system(f"python {os.getcwd()}/app.py")
except:
  ok = 'ok'