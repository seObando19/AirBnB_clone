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
from models.user import User


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

    def do_all(self, cls_name):
        """
            Prints all string representation of all instances based
            --------------------------------------------------------

        @ usage - > <data> <model> {ex: all BaseModel}
        """
        if not cls_name or cls_name in globals():
            for value in models.storage.all().values():
                print([str(value)])
        else:
            print("** class doesn't exist **")

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

    def do_update(self, arg):
        """
        update - update a parameter´s value
        -----------------------------------------------------

        @ usage - > <data> <model> <attribute> <value>
        {ex: update BaseModel 1223131424131 name MARCOS}
        """
        argumentos = arg.split()
        key = ".".join(argumentos[:2])
        if not argumentos:
            print("** class name missing **")
        elif argumentos[0] not in globals():
            print("** class doesn't exist **")
        elif len(argumentos) < 2:
            print("** instance id missing **")
        elif ".".join(argumentos[:2]) not in models.storage.all():
            print("** no instance found **")
        elif len(argumentos) < 3:
            print("** attribute name missing **")
        elif len(argumentos) < 4:
            print("** value missing **")
        else:
            key = ".".join(argumentos[:2])
            u_atributo = argumentos[2]
            u_valor = argumentos[3]
            _dict = models.storage.all()[key].__dict__
            _dict[u_atributo] = u_valor
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
