#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ The state class, contains class and getter attributes """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                               cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
                Getter attribute that returns list of City
                instances with state_id == State().id
            """
            city_list = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
