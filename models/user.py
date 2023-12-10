#!/usr/bin/python3

"""
This module contains the user class
"""


import uuid
import datetime as dt
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
