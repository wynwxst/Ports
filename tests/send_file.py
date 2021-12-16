from ports import APP, static_APP
from ports import tools


Ports = APP()
@Ports.route("/")
def index():
  return "Favicon Activated"
@Ports.route("/favicon.ico")
def favicon():
  return tools.send_file("favicon.ico")
Ports.run("0.0.0.0",8080)