#!/usr/bin/python3
"""This module defines a class to manage database storage for AirBnB clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """ This class manages storage of AirBnB models on a MySQL db server """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes a new engine using environment variables """
        env = os.environ
        user = env.get('HBNB_MYSQL_USER', 'hbnb_dev')
        passwd = env.get('HBNB_MYSQL_PWD')
        host = env.get('HBNB_MYSQL_HOST', 'localhost')
        db = env.get('HBNB_MYSQL_DB')
        environ = env.get('HBNB_ENV', 'dev')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                               format(user, passwd, host, db),
                               pool_pre_ping=True)

        if environ == "test":
            for table in self.__session:
                table.drop(self.__engine)

    def all(self, cls=None):
        """ Retrieves all model objects depending on class """
        obj_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls).order_by(cls.id).all():
                obj_dict.update({f"{cls.__name__}.{obj.id}": obj})
        else:
            for obj in self.__session.query(
                        User, State, City, Place, Amenity, Review).all():
                obj_dict.update({f"{obj.__class__.__name__}.{obj.id}": obj})
        return obj_dict

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes object from the current database session if it exists """
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """ Generates the database schema for all tables """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
