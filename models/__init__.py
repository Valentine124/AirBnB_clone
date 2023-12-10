#!/usr/bin/env python3

"""
Application initializer
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
