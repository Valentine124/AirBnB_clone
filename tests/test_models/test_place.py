#!/usr/bin/python3
""" test place """


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = Place()

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(Place, type(self.calc))
        self.assertEqual(str, type(self.calc.city_id))
        self.assertEqual(str, type(self.calc.user_id))
        self.assertEqual(str, type(self.calc.name))
        self.assertEqual(str, type(self.calc.description))
        self.assertEqual(int, type(self.calc.number_rooms))
        self.assertEqual(int, type(self.calc.max_guest))
        self.assertEqual(int, type(self.calc.number_bathrooms))
        self.assertEqual(int, type(self.calc.price_by_night))
        self.assertEqual(float, type(self.calc.latitude))
        self.assertEqual(float, type(self.calc.longitude))
        self.assertEqual(list, type(self.calc.amenity_ids))


if __name__ == '__main__':
    unittest.main()
