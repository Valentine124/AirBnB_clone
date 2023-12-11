#!/usr/bin/python3
""" test Consle """

import unittest
from console import HBNBCommand
from datetime import datetime
from models.base_model import BaseModel
import time


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.calc = HBNBCommand()


if __name__ == '__main__':
    unittest.main()
