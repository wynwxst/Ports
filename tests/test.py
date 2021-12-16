from ports import APP, static_APP,Core, localStorage
from ports import tools
import ports

app = APP()

@app.route("/")
def index():
  return tools.render_template("index.html",{"ip":tools.get_addr()})

@app.route("/hi/bye/")
def hibye():
  return "hi bye!"

@app.route("/hello/",args=["name"])
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

@app.route("/favicon.ico")
def favicon():
  return tools.send_file("www/indra.jpg")






ls = localStorage("webserve.ehnryu.repl.co")








app.run()
