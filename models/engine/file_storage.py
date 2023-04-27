#!/usr/bin/python3
"""This module defines a class to manage file storage for AirBnB clone"""
import json
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User,
           'State': State, 'City': City, 'Place': Place,
           'Amenity': Amenity, 'Review': Review}


class FileStorage:
    """This class manages storage of AirBnB models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls_dict = {}

        if cls:
            if type(cls) == str:
                cls = classes[cls]
            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    cls_dict[key] = obj
        else:
            cls_dict = self.__objects
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            if cls_dict:
                for v in cls_dict.values():
                    v.__dict__.pop('_sa_instance_state', None)
        return cls_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file at __file_path"""
        objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objs, f)

    def delete(self, obj=None):
        """Deletes object from __objects if it exists"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
            self.save()

    def reload(self):
        """Deserializes the JSON file at __file_path to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass

    def close(self):
        """Deseserializes JSON file to objects"""
        return self.reload()
