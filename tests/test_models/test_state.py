#!/usr/bin/python3
""" test State """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = State()

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(State, type(self.calc))
        self.assertEqual(str, type(self.calc.name))


if __name__ == '__main__':
    unittest.main()
