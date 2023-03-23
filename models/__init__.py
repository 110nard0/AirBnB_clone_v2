#!/usr/bin/python3
"""
This module creates an instance object of FileStorage or DBStorage type
and calls the reload method to retrieve saved model class instances
"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
