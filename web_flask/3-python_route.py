#!/usr/bin/python3
"""
Starts a small web aplication
- listening on 0.0.0.0 port 5000
- display "Hello HBNB!"

Task 1
-add route /hbnb
-display HBNB

Task 2
-add route /c/<text>
-display parameter received

Task 3
-crear una ruta alternativa
"""
from flask import Flask

app = Flask(__name__)
"""hacemos que las entradas sean flexible con los slashes (/)"""


@app.route("/", strict_slashes=False)
def hello_world():
    """en la ruta default de la aplicación display string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """rutear /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_parse(text):
    """ formatear el texto correctamente """
    parse_text = text.replace('_', ' ')
    return "{}".format(parse_text)


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_cool(text):
    """ Mostrar string por default sino se pasan parametros """
    parse_text = text.replace("_", " ")
    return "Python {}".format(parse_text)


"""la app no corre al ser importada"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
