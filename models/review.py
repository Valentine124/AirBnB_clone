#!/usr/bin/env python3

"""
This module contains the Review class
"""


import uuid
import datetime as dt
from datetime import datetime
from models.base_model import BaseModel


class Review(BaseModel):
    place_id: str = ''
    user_id: str = ''
    text: str = ''
