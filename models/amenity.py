#!/usr/bin/env python3

"""
This module contains the Amenity class
"""


import uuid
import datetime as dt
from datetime import datetime
from models.base_model import BaseModel


class Amenity(BaseModel):
    name: str = ''
