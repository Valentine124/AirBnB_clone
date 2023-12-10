#!/usr/bin/env python3

"""
This module contains the city class
"""


import uuid
import datetime as dt
from datetime import datetime
from models.base_model import BaseModel


class City(BaseModel):

    """
    This module contains the city class

    Attributes:
        state_id:string - state id
        name:string - name of city
    """

    state_id: str = ''
    name: str = ''
