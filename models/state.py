#!/usr/bin/python3
"""
    Implementation of the State class
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
        Implementation for the State.
    """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ""

        @property
        def cities(self):

            city_dict = models.storage.all(models.classes['City'])
            new_list = []

            for key, value in city_dict.items():
                if value.state_id == self.id:
                    new_list.append(value)
            return new_list
