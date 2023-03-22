#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The state class, contains class and getter attributes """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all,delete")

    @property
    def cities(self):
        """"""
        city_list = []
        for city in FileStorage.all(City).values():
            if city['state_id'] == self.id:
                city_list.append(city)
        return city_list
