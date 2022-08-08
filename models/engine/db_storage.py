#!/usr/bin/python3
"""
Class DBStorage:
- serializa las Instancias en nuestra base de datos
- deserializa las tablas de db a Instancias
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from models.amenity import Amenity
from sqlalchemy import (create_engine)

class DBStorage():
	"""class of database"""
	__engine = None
	__session = None

	def __init__(self):
		if __name__ == "__main__":
			self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
    		Base.metadata.create_all(engine)

		all(self, cls=None):
			"""peticion de todos los objetos"""
        	return self.__objects