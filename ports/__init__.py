ses = [
    {
        "code": "1xx",
        "phrase": "**Informational**",
        "description": "\"indicates an interim response for communicating connection status or request progress prior to completing the requested action and sending a final response.\" ~ [sure](http://www.urbandictionary.com/define.php?term=sure)",
        "spec_title": "RFC7231#6.2",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.2"
    },
    {
        "code": "100",
        "phrase": "Continue",
        "description": "\"indicates that the initial part of a request has been received and has not yet been rejected by the server.\"",
        "spec_title": "RFC7231#6.2.1",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.2.1"
    },
    {
        "code": "101",
        "phrase": "Switching Protocols",
        "description": "\"indicates that the server understands and is willing to comply with the client's request, via the Upgrade header field, for a change in the application protocol being used on this connection.\"",
        "spec_title": "RFC7231#6.2.2",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.2.2"
    },
    {
        "code": "2xx",
        "phrase": "**Successful**",
        "description": "\"indicates that the client's request was successfully received, understood, and accepted.\" ~ [cool](https://twitter.com/DanaDanger/status/183316183494311936)",
        "spec_title": "RFC7231#6.3",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3"
    },
    {
        "code": "200",
        "phrase": "OK",
        "description": "\"indicates that the request has succeeded.\"",
        "spec_title": "RFC7231#6.3.1",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3.1"
    },
    {
        "code": "201",
        "phrase": "Created",
        "description": "\"indicates that the request has been fulfilled and has resulted in one or more new resources being created.\"",
        "spec_title": "RFC7231#6.3.2",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3.2"
    },
    {
        "code": "202",
        "phrase": "Accepted",
        "description": "\"indicates that the request has been accepted for processing, but the processing has not been completed.\"",
        "spec_title": "RFC7231#6.3.3",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3.3"
    },
    {
        "code": "203",
        "phrase": "Non-Authoritative Information",
        "description": "\"indicates that the request was successful but the enclosed payload has been modified from that of the origin server's 200 (OK) response by a transforming proxy.\"",
        "spec_title": "RFC7231#6.3.4",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3.4"
    },
    {
        "code": "204",
        "phrase": "No Content",
        "description": "\"indicates that the server has successfully fulfilled the request and that there is no additional content to send in the response payload body.\"",
        "spec_title": "RFC7231#6.3.5",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3.5"
    },
    {
        "code": "205",
        "phrase": "Reset Content",
        "description": "\"indicates that the server has fulfilled the request and desires that the user agent reset the \"document view\", which caused the request to be sent, to its original state as received from the origin server.\"",
        "spec_title": "RFC7231#6.3.6",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.3.6"
    },
    {
        "code": "206",
        "phrase": "Partial Content",
        "description": "\"indicates that the server is successfully fulfilling a range request for the target resource by transferring one or more parts of the selected representation that correspond to the satisfiable ranges found in the requests's Range header field.\"",
        "spec_title": "RFC7233#4.1",
        "spec_href": "https://tools.ietf.org/html/rfc7233#section-4.1"
    },
    {
        "code": "3xx",
        "phrase": "**Redirection**",
        "description": "\"indicates that further action needs to be taken by the user agent in order to fulfill the request.\" ~ [ask that dude over there](https://twitter.com/DanaDanger/status/183316183494311936)",
        "spec_title": "RFC7231#6.4",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4"
    },
    {
        "code": "300",
        "phrase": "Multiple Choices",
        "description": "\"indicates that the target resource has more than one representation, each with its own more specific identifier, and information about the alternatives is being provided so that the user (or user agent) can select a preferred representation by redirecting its request to one or more of those identifiers.\"",
        "spec_title": "RFC7231#6.4.1",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4.1"
    },
    {
        "code": "301",
        "phrase": "Moved Permanently",
        "description": "\"indicates that the target resource has been assigned a new permanent URI and any future references to this resource ought to use one of the enclosed URIs.\"",
        "spec_title": "RFC7231#6.4.2",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4.2"
    },
    {
        "code": "302",
        "phrase": "Found",
        "description": "\"indicates that the target resource resides temporarily under a different URI.\"",
        "spec_title": "RFC7231#6.4.3",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4.3"
    },
    {
        "code": "303",
        "phrase": "See Other",
        "description": "\"indicates that the server is redirecting the user agent to a different resource, as indicated by a URI in the Location header field, that is intended to provide an indirect response to the original request.\"",
        "spec_title": "RFC7231#6.4.4",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4.4"
    },
    {
        "code": "304",
        "phrase": "Not Modified",
        "description": "\"indicates that a conditional GET request has been received and would have resulted in a 200 (OK) response if it were not for the fact that the condition has evaluated to false.\"",
        "spec_title": "RFC7232#4.1",
        "spec_href": "https://tools.ietf.org/html/rfc7232#section-4.1"
    },
    {
        "code": "305",
        "phrase": "Use Proxy",
        "description": "*deprecated*",
        "spec_title": "RFC7231#6.4.5",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4.5"
    },
    {
        "code": "307",
        "phrase": "Temporary Redirect",
        "description": "\"indicates that the target resource resides temporarily under a different URI and the user agent MUST NOT change the request method if it performs an automatic redirection to that URI.\"",
        "spec_title": "RFC7231#6.4.7",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.4.7"
    },
    {
        "code": "4xx",
        "phrase": "**Client Error**",
        "description": "\"indicates that the client seems to have erred.\" ~ [*you* fucked up](https://twitter.com/DanaDanger/status/183316183494311936)",
        "spec_title": "RFC7231#6.5",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5"
    },
    {
        "code": "400",
        "phrase": "Bad Request",
        "description": "\"indicates that the server cannot or will not process the request because the received syntax is invalid, nonsensical, or exceeds some limitation on what the server is willing to process.\"",
        "spec_title": "RFC7231#6.5.1",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.1"
    },
    {
        "code": "401",
        "phrase": "Unauthorized",
        "description": "\"indicates that the request has not been applied because it lacks valid authentication credentials for the target resource.\"",
        "spec_title": "RFC7235#6.3.1",
        "spec_href": "https://tools.ietf.org/html/rfc7235#section-3.1"
    },
    {
        "code": "402",
        "phrase": "Payment Required",
        "description": "*reserved*",
        "spec_title": "RFC7231#6.5.2",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.2"
    },
    {
        "code": "403",
        "phrase": "Forbidden",
        "description": "\"indicates that the server understood the request but refuses to authorize it.\"",
        "spec_title": "RFC7231#6.5.3",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.3"
    },
    {
        "code": "404",
        "phrase": "Not Found",
        "description": "\"indicates that the origin server did not find a current representation for the target resource or is not willing to disclose that one exists.\"",
        "spec_title": "RFC7231#6.5.4",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.4"
    },
    {
        "code": "405",
        "phrase": "Method Not Allowed",
        "description": "\"indicates that the method specified in the request-line is known by the origin server but not supported by the target resource.\"",
        "spec_title": "RFC7231#6.5.5",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.5"
    },
    {
        "code": "406",
        "phrase": "Not Acceptable",
        "description": "\"indicates that the target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.\"",
        "spec_title": "RFC7231#6.5.6",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.6"
    },
    {
        "code": "407",
        "phrase": "Proxy Authentication Required",
        "description": "\"is similar to 401 (Unauthorized), but indicates that the client needs to authenticate itself in order to use a proxy.\"",
        "spec_title": "RFC7235#3.2",
        "spec_href": "https://tools.ietf.org/html/rfc7235#section-3.2"
    },
    {
        "code": "408",
        "phrase": "Request Timeout",
        "description": "\"indicates that the server did not receive a complete request message within the time that it was prepared to wait.\"",
        "spec_title": "RFC7231#6.5.7",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.7"
    },
    {
        "code": "409",
        "phrase": "Conflict",
        "description": "\"indicates that the request could not be completed due to a conflict with the current state of the resource.\"",
        "spec_title": "RFC7231#6.5.8",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.8"
    },
    {
        "code": "410",
        "phrase": "Gone",
        "description": "\"indicates that access to the target resource is no longer available at the origin server and that this condition is likely to be permanent.\"",
        "spec_title": "RFC7231#6.5.9",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.9"
    },
    {
        "code": "411",
        "phrase": "Length Required",
        "description": "\"indicates that the server refuses to accept the request without a defined Content-Length.\"",
        "spec_title": "RFC7231#6.5.10",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.10"
    },
    {
        "code": "412",
        "phrase": "Precondition Failed",
        "description": "\"indicates that one or more preconditions given in the request header fields evaluated to false when tested on the server.\"",
        "spec_title": "RFC7232#4.2",
        "spec_href": "https://tools.ietf.org/html/rfc7232#section-4.2"
    },
    {
        "code": "413",
        "phrase": "Payload Too Large",
        "description": "\"indicates that the server is refusing to process a request because the request payload is larger than the server is willing or able to process.\"",
        "spec_title": "RFC7231#6.5.11",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.11"
    },
    {
        "code": "414",
        "phrase": "URI Too Long",
        "description": "\"indicates that the server is refusing to service the request because the request-target is longer than the server is willing to interpret.\"",
        "spec_title": "RFC7231#6.5.12",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.12"
    },
    {
        "code": "415",
        "phrase": "Unsupported Media Type",
        "description": "\"indicates that the origin server is refusing to service the request because the payload is in a format not supported by the target resource for this method.\"",
        "spec_title": "RFC7231#6.5.13",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.13"
    },
    {
        "code": "416",
        "phrase": "Range Not Satisfiable",
        "description": "\"indicates that none of the ranges in the request's Range header field overlap the current extent of the selected resource or that the set of ranges requested has been rejected due to invalid ranges or an excessive request of small or overlapping ranges.\"",
        "spec_title": "RFC7233#4.4",
        "spec_href": "https://tools.ietf.org/html/rfc7233#section-4.4"
    },
    {
        "code": "417",
        "phrase": "Expectation Failed",
        "description": "\"indicates that the expectation given in the request's Expect header field could not be met by at least one of the inbound servers.\"",
        "spec_title": "RFC7231#6.5.14",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.14"
    },
    {
        "code": "418",
        "phrase": "I'm a teapot",
        "description": "\"Any attempt to brew coffee with a teapot should result in the error code 418 I'm a teapot.\"",
        "spec_title": "RFC2324#2.3.1",
        "spec_href": "https://tools.ietf.org/html/rfc2324#section-2.3.1"
    },
    {
        "code": "426",
        "phrase": "Upgrade Required",
        "description": "\"indicates that the server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol.\"",
        "spec_title": "RFC7231#6.5.15",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.5.15"
    },
    {
        "code": "5xx",
        "phrase": "**Server Error**",
        "description": "\"indicates that the server is aware that it has erred or is incapable of performing the requested method.\" ~ [*we* fucked up](https://twitter.com/DanaDanger/status/183316183494311936)",
        "spec_title": "RFC7231#6.6",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6"
    },
    {
        "code": "500",
        "phrase": "Internal Server Error",
        "description": "\"indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.\"",
        "spec_title": "RFC7231#6.6.1",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6.1"
    },
    {
        "code": "501",
        "phrase": "Not Implemented",
        "description": "\"indicates that the server does not support the functionality required to fulfill the request.\"",
        "spec_title": "RFC7231#6.6.2",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6.2"
    },
    {
        "code": "502",
        "phrase": "Bad Gateway",
        "description": "\"indicates that the server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed while attempting to fulfill the request.\"",
        "spec_title": "RFC7231#6.6.3",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6.3"
    },
    {
        "code": "503",
        "phrase": "Service Unavailable",
        "description": "\"indicates that the server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay.\"",
        "spec_title": "RFC7231#6.6.4",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6.4"
    },
    {
        "code": "504",
        "phrase": "Gateway Time-out",
        "description": "\"indicates that the server, while acting as a gateway or proxy, did not receive a timely response from an upstream server it needed to access in order to complete the request.\"",
        "spec_title": "RFC7231#6.6.5",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6.5"
    },
    {
        "code": "505",
        "phrase": "HTTP Version Not Supported",
        "description": "\"indicates that the server does not support, or refuses to support, the protocol version that was used in the request message.\"",
        "spec_title": "RFC7231#6.6.6",
        "spec_href": "https://tools.ietf.org/html/rfc7231#section-6.6.6"
    },
    {
        "code": "102",
        "phrase": "Processing",
        "description": "\"is an interim response used to inform the client that the server has accepted the complete request, but has not yet completed it.\"",
        "spec_title": "RFC5218#10.1",
        "spec_href": "https://tools.ietf.org/html/rfc2518#section-10.1"
    },
    {
        "code": "207",
        "phrase": "Multi-Status",
        "description": "\"provides status for multiple independent operations.\"",
        "spec_title": "RFC5218#10.2",
        "spec_href": "https://tools.ietf.org/html/rfc2518#section-10.2"
    },
    {
        "code": "226",
        "phrase": "IM Used",
        "description": "\"The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.\"",
        "spec_title": "RFC3229#10.4.1",
        "spec_href": "https://tools.ietf.org/html/rfc3229#section-10.4.1"
    },
    {
        "code": "308",
        "phrase": "Permanent Redirect",
        "description": "\"The target resource has been assigned a new permanent URI and any future references to this resource outght to use one of the enclosed URIs. [...] This status code is similar to 301 Moved Permanently (Section 7.3.2 of rfc7231), except that it does not allow rewriting the request method from POST to GET.\"",
        "spec_title": "RFC7538",
        "spec_href": "https://tools.ietf.org/html/rfc7538"
    },
    {
        "code": "422",
        "phrase": "Unprocessable Entity",
        "description": "\"means the server understands the content type of the request entity (hence a 415(Unsupported Media Type) status code is inappropriate), and the syntax of the request entity is correct (thus a 400 (Bad Request) status code is inappropriate) but was unable to process the contained instructions.\"",
        "spec_title": "RFC5218#10.3",
        "spec_href": "https://tools.ietf.org/html/rfc2518#section-10.3"
    },
    {
        "code": "423",
        "phrase": "Locked",
        "description": "\"means the source or destination resource of a method is locked.\"",
        "spec_title": "RFC5218#10.4",
        "spec_href": "https://tools.ietf.org/html/rfc2518#section-10.4"
    },
    {
        "code": "424",
        "phrase": "Failed Dependency",
        "description": "\"means that the method could not be performed on the resource because the requested action depended on another action and that action failed.\"",
        "spec_title": "RFC5218#10.5",
        "spec_href": "https://tools.ietf.org/html/rfc2518#section-10.5"
    },
    {
        "code": "428",
        "phrase": "Precondition Required",
        "description": "\"indicates that the origin server requires the request to be conditional.\"",
        "spec_title": "RFC6585#3",
        "spec_href": "https://tools.ietf.org/html/rfc6585#section-3"
    },
    {
        "code": "429",
        "phrase": "Too Many Requests",
        "description": "\"indicates that the user has sent too many requests in a given amount of time (\"rate limiting\").\"",
        "spec_title": "RFC6585#4",
        "spec_href": "https://tools.ietf.org/html/rfc6585#section-4"
    },
    {
        "code": "431",
        "phrase": "Request Header Fields Too Large",
        "description": "\"indicates that the server is unwilling to process the request because its header fields are too large.\"",
        "spec_title": "RFC6585#5",
        "spec_href": "https://tools.ietf.org/html/rfc6585#section-5"
    },
    {
        "code": "451",
        "phrase": "Unavailable For Legal Reasons",
        "description": "\"This status code indicates that the server is denying access to the resource in response to a legal demand.\"",
        "spec_title": "draft-ietf-httpbis-legally-restricted-status",
        "spec_href": "https://tools.ietf.org/html/draft-ietf-httpbis-legally-restricted-status"
    },
    {
        "code": "506",
        "phrase": "Variant Also Negotiates",
        "description": "\"indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.\"",
        "spec_title": "RFC2295#8.1",
        "spec_href": "https://tools.ietf.org/html/rfc2295#section-8.1"
    },
    {
        "code": "507",
        "phrase": "Insufficient Storage",
        "description": "\"means the method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.\"",
        "spec_title": "RFC5218#10.6",
        "spec_href": "https://tools.ietf.org/html/rfc2518#section-10.6"
    },
    {
        "code": "511",
        "phrase": "Network Authentication Required",
        "description": "\"indicates that the client needs to authenticate to gain network access.\"",
        "spec_title": "RFC6585#6",
        "spec_href": "https://tools.ietf.org/html/rfc6585#section-6"
    },
    {
        "code": "7xx",
        "phrase": "**Developer Error**",
        "description": "[err](http://www.urbandictionary.com/define.php?term=err)",
        "spec_title": "7xx-rfc",
        "spec_href": "http://documentup.com/joho/7XX-rfc"
    }
]
def sp(s):
    s = str(s)
    for i in ses:
        if s == i["code"]:
            return i["code"] + " " + i["phrase"]
from typing import Callable, Dict, Optional, Pattern, Set, Tuple, List, Union
import re
import socket
import requests
import json
import io
import typing
from functools import partial
import random
from collections import defaultdict,namedtuple
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
import asyncio
import websockets



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
        from collections import namedtuple
        tr = namedtuple("tr",["method","path","headers","body","args"])
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
        args = {}
        a = {}
        if "?" in path:
            l = path.split("?")
            path = l[0]
            args = l[1]

            if "&" in args:
                args = args.split("&")
                for i in args:
                    lt = i.split("=")
                    a[lt[0]] = lt[1]
            else:
                i = args.split("=")
                a[i[0]] = i[1]

        request = tr(method=method.upper(), path=path, headers=headers, body=body,args=a)
        return request


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

      x = Response(status=sp(200),content=str(content))
      x.headers.add("Content-Type","application/json")
      return x

class Events:
    def kill(app):
        sock = app.sock
        app.running = False
        print("killing process..")
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return
class Socket:
    def __init__(self,app):
        self.app=app
        self.sockets = {}
        self.port = app.config["port"] + 1
        self.host = app.config["host"]
        self.insense = {}
        self.key = app.env.get("key","default")
    def connect(self,sock=None,content=None,path="/"):
        import ssl
        if path.startswith("/") == False:
            path = "/" + path
        async def dec(event,conn):
            ev = event.lower()
            if event == None:
                event = ""
            if event.startswith("event:") == False:
                event = "event:" + event
            if event == None and conn != None or event == "event:" and conn != None:
                event = conn
            if event != None and conn != None:
                event = event + " " + conn
            uri = f"ws://{self.host}:{self.port}" + path
            event += f"\nkey:{self.key}"
            async with websockets.connect(uri) as websocket:

                if "pre:" + ev in self.sockets:
                    event = self.sockets["pre:" + ev]()
                await websocket.send(event)
                if "post:" + ev in self.sockets:
                    event = self.sockets["post:" + ev]()


                greeting = await websocket.recv()
                return greeting
        return asyncio.run(dec(sock,content))



    # create handler for each connection
    def on(self,event) -> Callable[[RouteHandlerT], RouteHandlerT]:

        def decor(handler: RouteHandlerT) -> RouteHandlerT:

            self.sockets[event.lower()] = handler


        return decor

    async def handler(self,websocket, path):


        data = await websocket.recv()
        key = data.split("\nkey:")[-1]
        data = data.replace("\nkey:" + key,"")
        
        if key != self.key:
            return await websocket.send("")
        d = None
        x = data.split()
        f = False
        wf = False
        for i in x:
            if f == False:
                if i.lower().startswith("event:"):
                    d = i.replace("event:","")
                    f = True
                    data = data.replace(i + " ","",1)

        rep = "no response"


        if "*" in self.sockets and d == None or d == "*":
            rep = await self.sockets["*"](data,path)
            d = ""
            wf = True

        if d.lower() in self.sockets and wf == False:
            rep = await self.sockets[d.lower()](data,path)
            wf = True


        if wf == False:
            if "404" not in self.sockets:
                rep = "error: socket not found"
            else:
                rep = await self.sockets["404"](data,path)

        await websocket.send(rep)
    async def main(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()

    def run(self):
        print(f"Socket server listening on {self.host}:{self.port}")
        asyncio.run(self.main())

class Ports:
  running = True

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
  req_tr = namedtuple("tr",["method","path","headers","body","args"])
  Request = req_tr(method="", path="", headers={}, body="",args={})
  Headers = ""
  sendrn = False
  events = {}
  events["kill"] = Events.kill
  events[404] = "Route not found"
  events[500] = "internal error"
  @property
  def all_events():
      ev = []
      for v in Ports.events:
          ev.append(v)
      return ev
  def on(event) -> Callable[[RouteHandlerT], RouteHandlerT]:
      def decorator(handler: RouteHandlerT) -> RouteHandlerT:
          Ports.events[event] = handler
      return decorator
  def kill():
      Ports.events["kill"](Ports)




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

  def __call__(method,path,args,req) -> Response:

      k = {}
      handler = None
      if args == []:
        handler = Core.lookup(method, path,None)
      else:
        handler = Core.lookup(method, path,None)

      e = Ports.rargs[method][path] == []




      if handler is None:
          print("No handler")
          return "Route Not Found"
      if "req" in handler.func.__code__.co_varnames or "request" in handler.func.__code__.co_varnames:
          k["req"] = req
      return handler(**k)
      if e == True:
        return handler(**k)
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




        return handler(**k)








  def handle_request(request):
      if "request" in Ports.events:
          return Ports.events["request"](Ports,request)
      else:
          filename = request.path
          method = request.method
          args = None
          """Handles the HTTP request."""
          timern = datetime.now()

          print(f"{request.method} {request.path} at {timern}")
          args = request.args




          if filename.endswith("/") and filename != "/":
            filename = filename[:-1]
            args = []

            # keyerror cuz doesn't become just /hello


          if Ports.config["static"]:
            sdir = Ports.config["static_dir"]
            try:
              if filename == "/":
                filename = "index.html"
              fin = open(f'{sdir}/' + filename)
              content = fin.read()
              fin.close()
              response = '' + content
            except FileNotFoundError:
              response = 'File Not Found'


          else:
            sdir = Ports.config["static_dir"]
            if filename.startswith(f"/{sdir}/"):
              tose = filename.replace(f"/{sdir}/",f"{sdir}/")
              return tools.send_file(f"{tose}")

            print(f"PATH:'{filename}' | ARGS:'{args}'")
            if filename not in Ports.routes[method]:

              response = Response(status=sp(404), content=Ports.events[404])
            else:


              try:
                if Ports.templates[method][filename] != "":
                  fin = open('templates/' + Ports.templates[method][filename])
                  content = fin.read()
                  fin.close()

                  response = '' + content
                else:
                  try:

                    response = Ports.__call__(method,filename,args,request)

                  except Exception as e:
                    if "route_error" in Ports.events:
                        Ports.events["route_error"](e)
                    else:
                        print("FUNCTION ERROR: " + str(e))
                    response = Response(status="500 Internal Server Error", content=Ports.events[500])
              except FileNotFoundError:

                  response = Response(status=sp(404), content=Ports.events[404])

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

                        if type(response) != Response:
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
            if "bind" in Ports.events:
                Ports.events["bind"]()

            while Ports.running == True:
                try:
                    s = server_sock.accept()
                    if "listen" in Ports.events:

                        Ports.events["listen"](server_sock,s)
                    self.connection_queue.put(s)
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

def APP(name=__name__,sdir="static"):
  print(f"starting {name}!")
  Ports.config["static_dir"] = sdir
  Ports.config["name"] = name
  Ports.config["static"] = False
  globals.app = Ports
  return globals.app

def static_APP(name=__name__,path=""):
  print(f"starting {name}!")
  Ports.config["name"] = name
  Ports.config["static_dir"] = path

  Ports.config["static"] = True
  globals.app = Ports
  return globals.app

try:
  if sys.argv[1] == "run":
    os.system(f"python {os.getcwd()}/app.py")
except:
  ok = 'ok'
