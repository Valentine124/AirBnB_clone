#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User


all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

my_model = User()
my_mogfddel = User()
my_fgmodel = User()
masy_model = User()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
