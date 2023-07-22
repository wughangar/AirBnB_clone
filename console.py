#!/usr/bin/python3
"""
the airbnb console
"""

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import cmd


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
        elif cls_name not in globals():
            print("** class doesn't exist **")
        else:
            cls = globals().get(cls_name)
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg=None):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                dic = storage.all()

                if key not in dic:
                    print("** no instance found **")
                else:
                    print(dic[key])

    def do_destroy(self, arg=None):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                dic = storage.all()

                if key not in dic:
                    print("** no instance found **")
                else:
                    del dic[key]
                    storage.save()

    def do_all(self, arg=None):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        dic = storage.all()
        if not arg:
            for value in dic.values():
                print(value)
        else:
            cls = [key.split(".")[0] for key in dic]
            if arg not in cls:
                print("** class doesn't exist **")
            else:
                for key, value in dic.items():
                    if key.startswith(arg):
                        print(value)

    def do_update(self, arg=None):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            dic = storage.all()
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                if key not in dic:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if key in dic:
                    obj = dic[key]
                    setattr(obj, args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")

    def do_count(self, arg):
        """ Retuns count for a types' instances """
        dic = storage.all()
        count = 0
        for value in dic.values():
            if type(value).__name__ == arg:
                count += 1
        return count

    def default(self, arg):
        """ Sets default console behaviour """
        args = arg.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                print(self.do_count(args[0]))
            elif args[1].startswith("show"):
                ids = args[1].split("(")[1][1:-2]
                self.do_show(f"{args[0]} {ids}")
            elif args[1].startswith("destroy"):
                ids = args[1].split("(")[1][1:-2]
                self.do_destroy(f"{args[0]} {ids}")
            elif args[1].startswith("update"):
                parts = args[1].split("(")[1]
                parts = parts.split(",")
                ids = attr = value = ""
                if len(parts):
                    ids = parts[0][1:-1].strip()
                if len(parts) > 1:
                    attr = parts[1][1:-1].strip()
                if len(parts) > 2:
                    value = parts[2][:-1].strip()

                self.do_update(f"{args[0]} {ids} {attr} {value}")
            else:
                print(f"*** Unknown syntax: {arg}")
        else:
            print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
