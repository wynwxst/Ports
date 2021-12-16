from ports import APP, static_APP



Ports = APP()

@Ports.route("/")
def index():
  cookiejar = Ports.Cookies.get_all() # return in json name:value
  value = Ports.Cookies.get("pwd")
  if "username" in cookiejar:
    Ports.Cookies.delete("username")
  else:
    Ports.Cookies.set("username","example")

Ports.run("0.0.0.0",8080)