#!/usr/bin/python3
"""
    Implementation of the Amenity class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """
        Implementation for the Amenities.
    """
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place')
    else:
        name = ""
