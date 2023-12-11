#!/usr/bin/python3
""" test FileStorage """

import unittest
import models
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
import time


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.calc = FileStorage

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(FileStorage, self.calc)


if __name__ == '__main__':
    unittest.main()
