#!/usr/bin/python3
""" test User """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = User()

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(User, type(self.calc))
        self.assertEqual(str, type(self.calc.email))
        self.assertEqual(str, type(self.calc.password))
        self.assertEqual(str, type(self.calc.first_name))
        self.assertEqual(str, type(self.calc.last_name))


if __name__ == '__main__':
    unittest.main()
