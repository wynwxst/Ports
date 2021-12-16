import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ports import APP, static_APP



app = APP()

@app.route("/")
def index():
  
  return str(app.Cookies.get_all())
  

app.run("0.0.0.0",8080)