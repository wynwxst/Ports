from main import app, static_app,Core, localStorage
from main import tools
import main

Ports = app()

@Ports.route("/")
def index():
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






ls = localStorage("webserve.ehnryu.repl.co")








Ports.run()
