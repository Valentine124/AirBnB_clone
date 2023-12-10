#!/usr/bin/python3

import cmd


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

    def help_quit(self):
        """help doc for quit"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """handle EOF to exit command"""
        print()
        return True

    def help_EOF(self):
        """help doc for EOF"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
