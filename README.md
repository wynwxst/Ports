# PORTS
The modern flask alternative

# Installation
Simply install python and type `pip install Ports.py`

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
  cookiejar = Ports.Cookies.get_all() # return in json name:value
  value = Ports.Cookies.get("pwd")
  if "username" in cookiejar:
    Ports.Cookies.delete("username")
  else:
    Ports.Cookies.set("username","example")

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

Extensions:
"app.py"
```python
import ports
from ports import managers

app = ports.APP(__name__)
ext = managers.extensions
ext.register("extension.py")
# to register all "python" files in a directory:
#ext.regdir("extensions/")


@app.route("/exts/")
def exts():
  return "try route /"


app.run()
```
"extension.py"
```python
import ports
from ports import managers



class extension:
  def __init__(self,app):
    self.name = "name of extension"
    self.app = app
  def run(self):
    @self.app.route("/")
    def index():
      return "hi!"
    @self.app.route("/hello/")
    def hello():
      return str(self.app.config)

def setup(app):
  ext = extension(app)
  ext.run()
```
the object app is given to the function setup
similarly it can also be used as:
```python
import ports
from ports import managers

def extension(app):
  @app.route("/")
  def index():
    return "hi!"
  @app.route("/hello/")
  def hello():
    return str(app.config)

def setup(app):
  extension(app)
```
