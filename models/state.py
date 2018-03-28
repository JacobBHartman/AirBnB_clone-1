#!/usr/bin/python3
"""
    Implementation of the State class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
        Implementation for the State.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            new_list = []
            for key, value in storage.__objects():
                if value[state_id] == self.id and value[__class__] == 'City':
                    new_list.append(value)
            return new_list
    else:
        cities = relationship('City', backref='state', cascade='delete')

