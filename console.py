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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
