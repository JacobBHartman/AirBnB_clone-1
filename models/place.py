#!/usr/bin/python3
"""
    Define the class Place.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), nullable=False))
    


class Place(BaseModel, Base):
    """
        Define the class Place that inherits from BaseModel.
    """

    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """
            Returns list of Amenity instances based on amenity_ids
            """
            new_dict = models.storage.all(models.classes["Amenity"])
            for key, value in new_dict.items():
                if value.i
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """
            Handles append method for Amenity.id
            """
            self.amenity_ids = obj.id
            if obj.__class__.__name__ != 'Amenity':
                return
            append_dict = models.storage.all(obj)
            place_id = self.id
            for key, value in append_dict.items():
                if self.id == value.place_id:
                    self.amenity_ids.append(value.id)


        @property
        def review(self):
            """
            Returns a list of Review instances where the place_id is the same
            as the current Place.id
            """
            classchecker_dict = models.storage.all(models.classes["Review"])
            review_instances = []
            current = self.id
            for key, value in classchecker_dict.items():
                if value.place_id == current:
                    review_instances.append(value)
            return review_instances
