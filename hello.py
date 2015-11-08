
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, world."

if __name__ == "__main__":
  # Debug should be set to False on production machines. Setting Debug mode to True allows for a security
  # issue that can be used to execute arbitrary code. See the Flask documentation for more information.
  app.debug = False
  app.run(host='0.0.0.0')


