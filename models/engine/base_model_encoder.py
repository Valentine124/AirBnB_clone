#!/usr/bin/env python3

"""
This module contains the
encoder and decother function
for the base model class
"""

from models.base_model import BaseModel


def encode(obj):
    """
    Encoder for the base model
    class

    Args:
        obj:BaseModel - the object to decode
    """

    if isinstance(obj, BaseModel):
        return obj.__dict__
