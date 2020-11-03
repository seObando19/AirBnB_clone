#!/usr/bin/python3

"""
    HBNB
    Authors:
    - Andres Hurtado - github: @hurtadojara
    - Sebastian Obando - Github: @
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Console the Airbnb project'''
    prompt = "(hbnb) "

    def do_create(self, cls_name):
        """
        Create - Create new model from a class
        -----------------------------------------------------

        @ usage - > <data> <model> {ex: create BaseModel}
        """
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in globals():
            print("** class doesn't exist **")
        else:
            new_operacion = eval(cls_name)()
            print(new_operacion.id)
            new_operacion.save()

    def do_show(self, cls_name_id):
        """
        show - show Python object representation of json object
        -----------------------------------------------------

        @ usage - > <data> <model> <id> {ex: show BaseModel 123asd1272bn28dn}
        """
        name = cls_name_id.split()
        key = ".".join(name)
        if not name:
            print("** class name missing **")
        elif name[0] not in globals():
            print("** class doesn't exist **")
        elif len(name) == 1:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, cls_name_id):
        """
        destroy - destroy all list of json objects
        -----------------------------------------------------

        @ usage - > <data> <model> {ex: destroy BaseModel}
        """
        name = cls_name_id.split()
        key = ".".join(name)
        if not name:
            print("** class name missing **")
        elif name[0] not in globals():
            print("** class doesn't exist **")
        elif len(name) == 1:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            dic = models.storage.all()
            if key in dic:
                del dic[key]
                models.storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """exit the program\n"""
        print("")
        return True

    def emptyline(self):
        """Deactivate emptyline method from super class."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
