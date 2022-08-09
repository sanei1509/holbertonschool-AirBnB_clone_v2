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

    def all(self, cls=None):
        from models.base_model import BaseModel
        """ all """
        clases = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
        }
        cls_list = []
        if cls is None:
            cls_list.append(clases[cls])
        obj_dic = {}
        for clase in cls_list:
            all_data = self.__session.query(clase).all()
            for obj in all_data:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dic[key] = obj
        return obj_dic

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
        self.__session = Session()
