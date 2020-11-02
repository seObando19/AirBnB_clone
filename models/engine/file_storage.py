#!/usr/bin/python3
'''module used to store data'''
from models.base_model import BaseModel
import json
import os
class FileStorage:
    '''class for serialization and deserialization'''
    __file_path = "file.json" ##this have to be a string variable type
    __objects = {} ### disctionary type object
    def all(self):
        '''returns objects'''
        return self.__objects
    def new(self, obj):
        '''method to set new object in __object vriable'''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        '''method save'''
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            __dic = json.loads(self.__objects)
            ##Si no chequea bien hay que hacer sort al JSON
            json.dump(__dic, my_file, indent=4, default=str)
    def reload(self):
        '''Reload method'''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as my_file:
                __objects = json.load(my_file)
