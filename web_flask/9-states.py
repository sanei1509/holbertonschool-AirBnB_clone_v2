#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
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

Task 4
-mostrar solo si es un numero, ruta /number

Task 5
-renderizar un template

Task 6
-renderizar numeros impares

Task 8
-renderizar una lista de elementos con jinja

"""

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Function, que muestre el numero solo si es un entero"""
    return "{} is a number".format(n)


@app.route("/number_template/<n>", strict_slashes=False)
def render_html(n):
    """renderizar un template html"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def work_numbers(n):
    """ Trabajar numeros pasados por parametros en la pagina """
    return render_template('6-number_odd_or_even.html', number=n)


@app.teardown_appcontext
def off_all(self):
    """cerrar la sesión de SQL"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """ importando la data desde storage """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_and_cities(id=None):
    """importando la data desde storage"""
    states = storage.all(State).values()
    for state in states:
        if state in states:
            if state.id == id:
                return render_template("9-states.html", state=state)
    return render_template("9-states.html", state=None)


"""la app no corre al ser importada"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
