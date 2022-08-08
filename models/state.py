#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
