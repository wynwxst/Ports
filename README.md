# PORTS
The modern flask alternative

# Installation
Simply install python and type `pip install Ports.py`

# Usage

Start a static server in three lines:
```python
from main import APP, static_APP
Ports = static_APP()
Ports.run("0.0.0.0",8080)
```
then all files in `www/` will be hosted

Start a dynamic server:
```python
from ports import app, static_app


Ports = app()

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
from ports import app, static_app


Ports = app()
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
from ports import app, static_app, tools


Ports = app()

@Ports.route("/")
def index():
  return tools.render_template("index.html")

Ports.run("0.0.0.0",8080)
```
Renders `templates/index.html` ^

Arguments:
```python
from ports import app, static_app


Ports = app()

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

Send file:
```python
from ports import APP,tools
app = APP()

@app.route("/")
def index():
  tools.send_file("file.txt")
```



