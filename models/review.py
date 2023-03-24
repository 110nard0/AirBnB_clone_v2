#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablenames__ = "reviews"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
        place = relationship("Place")
    else:
        place_id = ""
        user_id = ""
        text = ""
