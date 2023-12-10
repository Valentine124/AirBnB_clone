#!/usr/bin/python3

"""HBNB console."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

MyClasses = {'BaseModel': BaseModel}


def sprate(arg=""):
    return arg.split()


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
        args = sprate(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in MyClasses:
            print("** class doesn't exist **")
        else:
            new = eval(args[0])()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = sprate(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in MyClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            s = "{}.{}".format(args[0], args[1])
            if s not in objects:
                print("** no instance found **")
            else:
                print(objects[s])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
