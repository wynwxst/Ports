from ports import APP, static_APP


Ports = APP()

@Ports.route("/")
def index(**args): # by default args will return {}
  if args == {}:
    return "No args"
  if "name" not in args:
    return "please give arg 'name'"
  name = args["name"]
  return f"hello {name}"
  

Ports.run("0.0.0.0",8080)