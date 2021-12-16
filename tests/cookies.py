from ports import APP, static_APP



Ports = APP()

@Ports.route("/")
def index():
  cokiejar = Ports.Cookies.get() # return in json name:value
  if "username" in cookiejar:
    Ports.Cookies.delete("username")
  else:
    Ports.cookies.set("username","example")

Ports.run("0.0.0.0",8080)