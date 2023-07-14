#!/usr/bin/python3
"""
the airbnb console
"""


from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
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
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                dic = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key not in dic:
                    cls = globals().get(args[0])
                    if cls:
                        obj = cls()
                        setattr(obj, args[2], args[3])
                else:
                    obj = dic[key]
                    setattr(obj, args[2], args[3])

                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
