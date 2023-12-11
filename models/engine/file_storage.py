#!/usr/bin/python3

"""
This module contains the `FileStorage
class for the application storage
"""


import json
import os.path
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


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

        return self.__objects

    def new(self, obj):
        """
        sets in `__objects` the `obj`
        with key `<obj class name>.id`

        Args:
            obj:<class name> - The object to save
        """
        if obj:
            s = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[s] = obj

    def save(self):
        """
        Serializes `__objects` to JSON file
        """
        with open(self.__file_path, 'w') as fp:
            res = {}
            for key, val in self.__objects.items():
                res[key] = val.to_dict()
            json.dump(res, fp)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        if `__file_path` exist
        """
        try:
            with open(self.__file_path, 'r') as fp:
                data = json.load(fp)

            for key, val in data.items():
                s = val['__class__']
                obj = eval(s)(**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
