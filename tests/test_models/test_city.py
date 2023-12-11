#!/usr/bin/python3
""" test city """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = City()

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(City, type(self.calc))
        self.assertEqual(str, type(self.calc.state_id))
        self.assertEqual(str, type(self.calc.name))


if __name__ == '__main__':
    unittest.main()
