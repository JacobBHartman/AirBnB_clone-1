#!/usr/bin/python3
"""
    Define the class Place.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from os import getenv


class Place(BaseModel, Base):
    """
        Define the class Place that inherits from BaseModel.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(cities.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def reviews(self):
            new_list = []
            for key, value in storage.__objects():
                if value[place_id] == self.id and value[__class__] == 'City':
                    new_list.append(value)
            return new_list
    else:
        reviews = relationship('Review', backref='place', cascade='delete')
