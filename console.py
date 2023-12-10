#!/usr/bin/python3

"""HBNB console."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime

MyClasses = ['BaseModel', 'User']


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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
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
                del objects[s]
                storage.save()

    def do_all(self, arg):
        args = sprate(arg)
        opj = MyClasses
        res = []

        if len(args):
            if args[0] not in MyClasses:
                print("** class doesn't exist **")
                return 0
            opj = [args[0]]

        for m in storage.all().values():
            if m.__class__.__name__ in opj:
                res.append(m.__str__())
        print(res)

    def do_all(self, arg):
        args = sprate(arg)
        opj = MyClasses
        res = []

        if len(args):
            if args[0] not in MyClasses:
                print("** class doesn't exist **")
                return 0
            opj = [args[0]]

        for m in storage.all().values():
            if m.__class__.__name__ in opj:
                res.append(m.__str__())
        print(res)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id."""
        args = sprate(arg)

        if len(args) == 0:
            print("** class name missing **")
            return 0
        elif args[0] not in MyClasses:
            print("** class doesn't exist **")
            return 0
        elif len(args) == 1:
            print("** instance id missing **")
            return 0

        objects = storage.all()
        s = "{}.{}".format(args[0], args[1])
        if s not in objects:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return 0
        elif len(args) == 3:
            print("** value missing **")
            return 0

        X = objects[s]

        X.__dict__[args[2]] = args[3]
        X.updated_at = datetime.utcnow()
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
