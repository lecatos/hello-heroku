from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
  return str( [(int(p), c) for p, c in [x.rstrip('\n').split(' ', 1) for x in os.popen('ps h -eo pid:1,command')]] ) + os.environ["PORT]
