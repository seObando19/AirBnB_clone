#!/usr/bin/python3

import cmd
'''Import the module cmd for the console'''
"""     intro = "Welcome the Console Airbnb" """


class HBNBCommand(cmd.Cmd):
    '''Console the Airbnb project'''
    prompt = "(hbnb) "

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