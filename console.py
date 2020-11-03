#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
'''Import the module cmd for the console'''


class HBNBCommand(cmd.Cmd):
    '''Console the Airbnb project'''
    prompt = "(hbnb) "

    def do_create(self, cls_name):
        ' Creates a new instance of BaseModel, saves it'
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in globals():
            print("** class doesn't exist **")
        else:
            new_operacion = eval(cls_name)()
            print(new_operacion.id)
            new_operacion.save()

    def do_show(self, cls_name_id):
        '''Prints the string representation of an
         instance based on the class name and id'''
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

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        '''exit the program\n'''
        print("")
        return True

    def emptyline(self):
        """Deactivate emptyline method from super   class."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
