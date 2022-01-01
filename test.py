import main
from main import managers

app = main.APP(__name__)
ext = managers.extensions
ext.register("testfiletwo.py")


@app.route("/exts/")
def exts():
  return "try route /"


app.run()
