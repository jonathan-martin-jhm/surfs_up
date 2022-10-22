# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# create flask route
@app.route("/")
def hello_world():
    return "Hello world"



