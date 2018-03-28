#!/usr/bin/python3
"""
    Define the class City.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """
        Define the class City that inherits from BaseModel.
    """
    __tablename__ = 'cities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        name = ""
        state_id = ""
