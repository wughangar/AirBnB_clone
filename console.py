#!/usr/bin/python3
"""
the airbnb console
"""

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

    def do_create(self, arg):
        """
        create command that creates a new instance of BaseModel, saves to 
        Json and prints the id
        """
        commands = arg.split(' ')
        class_name = commands[0].strip()
        if class_name == "":
            print("** class name missing **")
        elif class_name not in globals():
            print("** class doesnt exist **")
        else:
            cls = globals().get(class_name)
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ prints str rep on an isntance of a class"""
        commands = arg.split(' ')

        class_name = commands[0].strip()
        if class_name == "":
            print("** class name missing **")
        elif class_name not in globals():
            print("** class doesn't exist **")
        id = commands[1].strip()

        if id == "":
            print("** instance id missing **")
        elif class_name not in globals():
            print("** no instance found **")
        else:
            cls = globals().get(class_name)
            obj =cls()
            print(obj.__str__)

            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
