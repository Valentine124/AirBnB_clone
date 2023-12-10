#!/usr/bin/env python3

"""
This module contains the State class
"""


import uuid
import datetime as dt
from datetime import datetime
from models.base_model import BaseModel


class State(BaseModel):
    name: str = ''
