from main import app, static_app,Core, localStorage
from main import tools

Ports = app()

@Ports.route("/")
def index():
  from http import cookies
  C = cookies.SimpleCookie()
  C["hi"] = "ello"
  return tools.render_template("index.html")


@Ports.route("/hello/{name}")
def hello(name):
  return f"hello {name}"

Ports.env["todo"] = "ADD {} ARGS"

ls = localStorage("webserve.ehnryu.repl.co")








Ports.run("0.0.0.0",8080)
