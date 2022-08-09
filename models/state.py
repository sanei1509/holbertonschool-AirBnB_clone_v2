#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    type_storage = os.getenv("HBNB_TYPE_STORAGE")
    __tablename__ = "states"

    
    if type_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""
        
    @property
    def cities(self):
        """devolver una lista de instancias de city"""
        inst_list = []
        list_objects = models.storage.all(City)
        for city in list_objects.values():
            if city.state_id == self.id:
                inst_list.append(city)
        return inst_list
