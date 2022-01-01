import main
from main import managers
#from test import app


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
