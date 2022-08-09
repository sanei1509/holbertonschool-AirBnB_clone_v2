#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), nullable=False,)
    name = Column(String(128), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", cascade="all,delete", backref='cities')
