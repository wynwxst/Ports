from main import APP, static_APP,Core, localStorage
from main import tools
import main

Ports = APP()

@Ports.route("/")
def index():
  return tools.render_template("index.html",{"ip":tools.get_addr()})

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
