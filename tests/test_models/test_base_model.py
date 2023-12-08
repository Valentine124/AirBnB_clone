#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.calc = BaseModel()

    def testTypes(self):
        ''' to test type of all instanse '''
        self.assertEqual(BaseModel, type(self.calc))
        self.assertEqual(str, type(self.calc.id))

    def testId(self):
        # test uniq id
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)


if __name__ == '__main__':
    unittest.main()
