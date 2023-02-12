#!/usr/bin/python3
""" This module defines a class `HBNBCommand` """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

    def do_quit(self, arg):
        """  to exit the program """
        return True

    def do_EOF(self, arg):
        """  to exit the program """
        return True

    def emptyline(self):
        """  shouldn’t execute anything """
        return

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)
        storage.save()
        
    def do_show(self, arg):
        """ Prints the strinig representation of an
            instance based on the class name and id 

            usage: show <class_name> <object_id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
