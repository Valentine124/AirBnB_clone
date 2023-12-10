#!/usr/bin/python3

"""HBNB console."""

import cmd
import re
from shlex import split
from models.base_model import BaseModel

MyClasses = {'BaseModel':BaseModel}

def sprate(arg=""):
    return [i.strip(",") for i in split(arg)]

class HBNBCommand(cmd.Cmd):
    """AIRBNB command interpreter.

    Attributes:
        prompt (str): command prompt.
    """

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """handle EOF to exit command"""
        print()
        return True

    def do_creat(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in MyClasses:
            print("** class doesn't exist **")
        else:
            new = MyClasses[args[0]]()
            new.save()
            print(new.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
