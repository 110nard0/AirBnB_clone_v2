#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenity class provides attributes for place amenities """
    name = ""


"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel):
    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place")
    else:
        name = ""
"""
