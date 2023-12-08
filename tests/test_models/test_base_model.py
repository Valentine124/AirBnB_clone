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
        self.assertLess(a.updated_at, b.updated_at)

    def test_save(self):
        a = BaseModel()
        t1 = a.updated_at
        time.sleep(0.05)
        a.save()
        self.assertLess(t1, a.updated_at)
    
    def test_model_to_dic(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        for key in my_model_json.keys():
            if key == '__class__':
                self.assertEqual(my_model_json[key], my_model.__class__.__name__)
            elif key in ['created_at', 'updated_at']:
                s1 = str(my_model.__dict__[key].strftime("%Y-%m-%dT%H:%M:%S.%f"))
                self.assertEqual(s1, my_model_json[key])
            else:
                self.assertEqual(my_model_json[key], my_model.__dict__[key])

    def test_model_from_dic(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        print("JSON of my_model:")

        my_new_model = BaseModel(**my_model_json)

        for key in my_model_json.keys():
            if key not in ['__class__']:
                self.assertEqual(my_model.__dict__[key], my_new_model.__dict__[key])
                


if __name__ == '__main__':
    unittest.main()
