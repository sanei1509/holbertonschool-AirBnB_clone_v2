#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    def cities(self):
        """devolver una lista de instancias de city"""
        inst_list = []
        list_objects = storage.all(City)
        for key, value in list_objects.items():
            if value.state_id == self.id:
                inst_list.append(list_objects[key])
        return inst_list
