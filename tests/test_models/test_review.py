#!/usr/bin/python3
""" test Review """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = Review()

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(Review, type(self.calc))
        self.assertEqual(str, type(self.calc.place_id))
        self.assertEqual(str, type(self.calc.user_id))
        self.assertEqual(str, type(self.calc.text))


if __name__ == '__main__':
    unittest.main()
