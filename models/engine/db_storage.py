#!/usr/bin/python3
"""
Class DBStorage:
- serializa las Instancias en nuestra base de datos
- deserializa las tablas de db a Instancias
"""
import json
import os

from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from models.amenity import Amenity


class DBStorage():
    """class of database"""
    __engine = None
    __session = None

    def __init__(self):
        """Inicializamos """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      os.getenv("HBNB_MYSQL_USER"),
                                      os.getenv("HBNB_MYSQL_PWD"),
                                      os.getenv("HBNB_MYSQL_HOST"),
                                      os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        val_env = os.getenv("HBNB_ENV")
        if val_env == "test":
            Base.metadata.drop_all(self.__engine)

    # def all(self, cls=None):
    #     """peticion de todos los objetos"""
    #     obj_dic = {}
    #     if not cls:
    #         clases = ["User", "State", "City", "Amenity", "Place", "Review"]
    #         for x in clases:
    #             all_data = self.__session.query(x)
    #             key = x + "." + x.id
    #             obj_dic[key] = x
    #         return obj_dic
    #     else:
    #         data = self.__session.query(cls).all()
    #         for obj in data:
    #             key = cls.__name__ + "." + obj.id
    #             obj_dic[key] = obj
    #         return obj_dic

    def all(self, cls=None):
        """
        def method all that return all objects depending of the class name
        or return all if no class name is passed.
        """
        dic_return = {}
        classes = {
                'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }
        # Si no se pasa una clase, es porque se quiere todos los datos
        if cls is None:
            for clase in classes:
                # Se obtiene la data en la query por todas las clases
                data = self.__session.query(classes[clase]).all()
                for obj in data:
                    # Se obtiene la key para setear el obj en el dic a retornar
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    # Se agregan los objetos en el diccionario a retornar
                    dic_return[key] = obj
            return dic_return
        else:
            # Esto es para cuando se pasa un clase especifica:
            if classes[cls.__name__]:
                # Se obtiene la data en la query por todas las clases
                objects = self.__session.query(classes[cls.__name__]).all()
                for obj in objects:
                    key = type(obj).__name__ + '.' + obj.id
                    dic_return[key] = obj
            return dic_return

    def new(self, obj):
        '''add the boj to current db session'''
        self.__session.add(obj)

    def save(self):
        '''commit changes of the current db'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from current db session'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in the db and starts the session"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session

    def close(self):
        '''
        method that close the session
        '''
        self.__session.remove()
