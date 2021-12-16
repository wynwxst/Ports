from ports import APP, static_APP


Ports = APP()
Ports.env["key"] = "example"

Ports.db["visits"] = {}

@Ports.route("/")
def index():
  Ports.db["visits"] += 1
  return "hi!"

Ports.run("0.0.0.0",8080)