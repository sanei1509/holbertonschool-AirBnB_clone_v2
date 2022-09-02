#!/usr/bin/python3
from flask import Flask, render_template, request
from models import storage
from models.state import State
from models import storage
from models.amenity import Amenity
from models.place import Place
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

Task 10
- renderizar un contenido html completo del clon
"""
app = Flask(__name__)


@app.teardown_appcontext
def off_all(self):
    """Cierro la sesión de my sql"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filtro_data():
    """Contenido a mostra en la página html"""
    states = storage.all(State).values()
    lista_ams = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=lista_ams)
