# PORTS
The modern flask alternative

Start a static server in three lines:
```python
from main import app, static_app
Ports = static_app()
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
  tools.render_template("index.html")

Ports.run("0.0.0.0",8080)
```
Renders `templates/index.html` ^