from main import app, static_app,Core, localStorage
from main import tools

Ports = app()

@Ports.route("/")
def index():
  from http import cookies
  C = cookies.SimpleCookie()
  C["hi"] = "ello"
  return tools.render_template("index.html")

@Ports.route("/hi/bye/")
def hibye():
  return "hi bye!"

@Ports.route("/hello/",args=["name"])
def hello(**args):
  params = args
  name = ":("

  if params == {} or params == None:
    name = ""
  elif "name" not in params:
    name = "NOT GIVEN :("
  else:
    name = params["name"]
  return f"hello {name}"


Ports.env["todo"] = "ADD {} ARGS"

Ports.env["todo"] = "dargs partial 2nd arg on it"

ls = localStorage("webserve.ehnryu.repl.co")








Ports.run("0.0.0.0",8080)
