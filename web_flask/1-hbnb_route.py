#!/usr/bin/python3
from flask import Flask
"""
Starts a small web aplication
- listening on 0.0.0.0 port 5000
- display "Hello HBNB!"

Task 1
-add route /hbnb
-display HBNB
"""
app = Flask(__name__)
"""hacemos que las entradas sean flexible con los slashes (/)"""


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


"""la app no corre al ser importada"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)