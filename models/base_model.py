#!/usr/bin/env python3

"""
This module contains the base model
class which other classes will
inherit from
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    This base model class defines
    all common attributes/methods
    for other classes

    Attributes:
        id:string - id for each instance created
        created_at:datetime - assign with the current
            datetime when an instance is created
        updated_at:datetime - assign with the current
            datetime when an instance is created and
            it will be updated every time you change your object
    """

    def __init__(self):
        """
        The class initializer
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Overriding the str method
        """

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Update the public instance attribute
        `updated_at` with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing
        all keys/values of __dict__ of
        the instance
        """

        my_dict = {}
        dict = self.__dict__

        my_dict['__class__'] = f'{self.__class__.__name__}'

        for key, value in dict.items():
            if key == 'created_at' or key == 'updated_at':
                my_dict[key] = str(value.strftime("%Y-%m-%dT%H:%M:%S.%f"))
                continue
            my_dict[key] = value

        return my_dict
