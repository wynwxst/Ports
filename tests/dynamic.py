from ports import APP, static_APP


Ports = APP()

@Ports.route("/")
def index():
  return "hi!"

Ports.run("0.0.0.0",8080)