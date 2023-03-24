#!/usr/bin/python3
"""This module defines a base class for all models in our AirBnB clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

Base = declarative_base()


class BaseModel:
    """A base class for all AirBnB models with public attributes and methods"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(str(v)))
                else:
                    setattr(self, k, v)
                    self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the class instance"""
        return '[{}] ({}) {}'.format(
                              self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns the official string representation of instance object"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Converts instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary.update({'__class__': type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
