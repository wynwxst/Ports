from ports import APP, static_APP, tools


Ports = APP()

@Ports.route("/")
def index():
  return tools.render_template("index.html")

Ports.run("0.0.0.0",8080)