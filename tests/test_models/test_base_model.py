#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import time

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = BaseModel()

    def test_types(self):
        ''' to test type of all instanse '''
        self.assertEqual(BaseModel, type(self.calc))
        self.assertEqual(str, type(self.calc.id))
        self.assertEqual(datetime, type(self.calc.created_at))
        self.assertEqual(datetime, type(self.calc.updated_at))

    def test_id(self):
        # test uniq id
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_created__at(self):
        a = BaseModel()
        time.sleep(0.05)
        b = BaseModel()
        self.assertLess(a.created_at, b.created_at)


if __name__ == '__main__':
    unittest.main()
