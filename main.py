#Ports/__init__.py
from ports import APP, static_APP,Core, localStorage,Response,HTTPWorker
from ports import tools
import ssl
import socket

from ports import Socket
from taskel import Tasks
s = "x"
tm = Tasks()

app = APP()






@app.route("/")
def index(req):
    tg = req.args.get("greet","no greeting :(")
    return s.connect(sock="connect",content=tg,path="index")
@app.route("/req/")
def requ(req):
    return f"{req.method} at {req.path} with args as {req.args} and headers:\n{req.headers._headers}"
@app.route("/resp")
def respo():
    resp = Response(status="200 OK", content="hello world thru resp")
    resp.headers.add("key","value")

    return resp
@app.route("/kill")
def killer():
    app.kill()
    return "killed!"

def run():
    app.run(port=8181)



t = tm.create(target=run,daemon=True)
t.start()
s = Socket(app)

@s.on("connect")
async def all(data,path):
    if path == "/index":
        return "custom hello for / due to path " + data

    print("received! - " + data)
    return "data : " + data

s.run()

socketrun()
while True:
    p = app.config["port"]
    h = app.config["host"]
    x = input(f"{h}:{p} > ")
    if x in ["exit","kill","q","quit"]:
        app.kill()
        t.stop()
        break
