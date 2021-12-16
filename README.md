# PORTS
The modern flask alternative

# Installation
Simply install python and type `pip install PortsPy`

# Usage

Start a static server in three lines:
```python
from ports import APP, static_APP
Ports = static_APP()
Ports.run("0.0.0.0",8080)
```
then all files in `www/` will be hosted

Start a dynamic server:
```python
from ports import APP, static_APP


Ports = APP()

@Ports.route("/")
def index():
  return "hi!"

Ports.run("0.0.0.0",8080)

```
Access localstorage:
```python
from ports import localStorage
ls = localStorage("yourwebsite.com","JSON") #sqlite and text are avaliable
```
localStorage Options:


localStorage.getItem(item)

localStorage.setItem(item, value)

localStorage.removeItem(item)

localStorage.clear()

Use a .env  and a json db system:
```python
from ports import APP, static_APP


Ports = APP()
Ports.env["key"] = "example"

Ports.db["visits"] = {}

@Ports.route("/")
def index():
  Ports.db["visits"] += 1
  return "hi!"

Ports.run("0.0.0.0",8080)
```

Template rendering:
```python
from ports import APP, static_APP, tools


Ports = APP()

@Ports.route("/")
def index():
  return tools.render_template("index.html")

Ports.run("0.0.0.0",8080)
```
Renders `templates/index.html` ^

Arguments:
```python
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
```

Cookies:
```python
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
```

Send file:
```python
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
```