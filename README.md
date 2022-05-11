# PORTS
A scalable, customizable, configurable, programmable, webserver framework

# Installation
Simply install python and type `pip install ports.py`

# Usage

Start a static server in three lines:
```python
from ports import APP, static_APP
app = static_APP()
app.run()
```
then all files in `www/` will be hosted

Start a dynamic server:
```python
from ports import APP, static_APP


app = APP()

@app.route("/")
def index():
  return "hi!"
@app.route("/hi/") # unlike flask you can put either /hi or /hi/ and it will work fine
def hi():
  return "hello"
@app.route("/bye") # will still work
def bye():
  return "bye"

app.run()

```

Make your own handler/framework:
```python
from ports import APP, static_APP, tools


app = APP()
app.on("request")
def frame(app,req):
  if req.method == "GET":
    if req.path == "/":
      return "Index (/)"
app.run()
```

Make a response:
```python
from ports import APP, static_APP, tools, Response


app = APP()
app.route("/")
def index():
  resp = Response(status="200 OK", content="hello world thru resp")
  resp.headers.add("key","value")
  return resp
app.run()
```

Events:
```python
from ports import APP, static_APP, tools, Response


app = APP()
app.route("/")
def index():
  resp = Response(status="200 OK", content="hello world thru resp")
  resp.headers.add("key","value")
  return resp
@app.on("bind")
def binded(sock):
  print("connected")
# all events can be accessed through app.all_events
app.run()
```

Template rendering:
```python
from ports import APP, static_APP, tools


app = APP()

@app.route("/")
def index():
  return tools.render_template("index.html")

app.run("0.0.0.0",8080)
```
Renders `templates/index.html` ^

Arguments:
```python
from ports import APP, static_APP


app = APP()

@app.route("/")
def index(req):
  if req.args == {}:
    return "No args"
  if "name" not in req.args:
    return "please give arg 'name'"
  name = req.args["name"]
  return f"hello {name}"


app.run("0.0.0.0",8080)
```

Cookies:
```python
from ports import APP, static_APP



app = APP()

@app.route("/")
def index():
  cookiejar = app.Cookies.get_all() # return in json name:value
  value = app.Cookies.get("pwd")
  if "username" in cookiejar:
    app.Cookies.delete("username")
  else:
    app.Cookies.set("username","example")

app.run("0.0.0.0",8080)
```

Send file:
```python
from ports import APP, static_APP
from ports import tools


app = APP()
@app.route("/")
def index():
  return "Favicon Activated"
@app.route("/favicon.ico")
def favicon():
  return tools.send_file("favicon.ico")
app.run("0.0.0.0",8080)
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
