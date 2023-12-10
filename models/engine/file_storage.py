#!/usr/bin/env python3

"""
This module contains the `FileStorage
class for the application storage
"""


import json
import os.path
from models.engine.base_model_encoder import encode


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

        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(FileStorage.__objects, fp, default=encode)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        if `__file_path` exist
        """

        file_exist = os.path.exists(FileStorage.__file_path)

        if file_exist:
            with open(FileStorage.__file_path, 'r') as fp:
                json.load(fp)
