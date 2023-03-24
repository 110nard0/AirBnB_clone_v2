#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"

        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        '''
        places = relationship("Place", back_populates="user",
                               cascade="all, delete, delete-orphan")
        reviews = relationship("Review", back_populates="user",
                                cascade="all, delete, delete-orphan")
        '''
    else:
        first_name = ""
        last_name = ""
        email = ""
        password = ""
