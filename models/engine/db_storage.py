#!/usr/bin/python3
"""This module defines a class to manage database storage for AirBnB clone"""
from models.base_model import BaseModel, BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {'User': User, 'State': State,
           'City': City, 'Place': Place,
           'Amenity': Amenity, 'Review': Review}


class DBStorage():
    """ This class manages storage of AirBnB models on a MySQL db server """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes a new engine using environment variables """
        # create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                       format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)
        # drop tables if test environment
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Retrieves all model objects depending on class """
        obj_dict = {}

        if not self.__session:
            self.reload()
        if type(cls) == str and cls in classes:
            cls = classes[cls]

        if cls:
            for obj in self.__session.query(cls).all():
                obj_dict.update({"{}.{}".
                                  format(cls.__name__, obj.id): obj})
        else:
            for val in classes.values():
                for obj in self.__session.query(val):
                    obj_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        if obj_dict:
            for v in obj_dict.values():
                v.__dict__.pop('_sa_instance_state', None)
        return obj_dict

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes object from the current database session if it exists """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Generates the database schema for all tables """
        # create session from current engine
        Base.metadata.create_all(self.__engine)
        # create database tables
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
