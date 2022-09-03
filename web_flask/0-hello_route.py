#!/usr/bin/python3
from flask import Flask
"""
Starts a small web aplication
- listening on 0.0.0.0 port 5000
- display "Hello HBNB!"
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """en la ruta default de la aplicación display string"""
    return "Hello HBNB!"


"""la app no corre al ser importada"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
