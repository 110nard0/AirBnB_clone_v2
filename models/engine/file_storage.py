#!/usr/bin/python3
"""This module defines a class to manage file storage for AirBnB clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
           'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review
          }


class FileStorage:
    """This class manages storage of AirBnB models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            cls_list = {}
            for key, obj in self.__objects.items():
                if key.split('.')[0] == cls:
                    cls_list[key] = obj
            return cls_list
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes object from __objects if it exists"""
        if obj is not None:
            dic = {}
            dic.update(self.all())
            for key, val in dic.items():
                if val == obj:
                    del FileStorage.__objects[key]
                    self.save()
        else:
            pass

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            obj_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
