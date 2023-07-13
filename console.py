#!/usr/bin/python3
"""
the airbnb console
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    main class defination for the console
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """to exit the program"""
        return True

    def emptyline(self):
        """when no commad is entered nothing happens"""
        pass

    def do_create(self, cls_name):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not cls_name:
            print("** class name missing **")
        elif cls_name != 'BaseModel':
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
