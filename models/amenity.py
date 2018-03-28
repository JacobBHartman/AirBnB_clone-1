#!/usr/bin/python3
"""
    Implementation of the Amenity class
"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Amenity(BaseModel):
    """
        Implementation for the Amenities.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
