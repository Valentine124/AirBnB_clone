#!/usr/bin/env python3

"""
This module contains the `FileStorage
class for the application storage
"""


import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity

class FileStorage:
    """
    This is the blueprint of the
    file storage object used to
    atore and retreive oject instances

    Attributes:
        __file_path:string - path to json file
        __objects:dictionary -
        empty but will store all objects by <class name>.id
    """

    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """
        Returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in `__objects` the `obj`
        with key `<obj class name>.id`

        Args:
            obj:<class name> - The object to save
        """

        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Serializes `__objects` to JSON file
        """
        res = {}
        lit = FileStorage.__objects
        for key, val in lit.items():
            res[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w') as fp:

            json.dump(res, fp)


    def reload(self):
        """
        Deserializes the JSON file to __objects
        if `__file_path` exist
        """
        try:
            with open(FileStorage.__file_path, 'r') as fp:
                data = json.load(fp)

            for key, val in data.items():        
                s = val['__class__']
                obj = eval(s)(**val)
                self.__objects[key] = obj
        except:
            pass
