#!/usr/bin/python3
'''module used to store data'''
from models.base_model import BaseModel
import json
import os


class FileStorage:
    '''class for serialization and deserialization'''
    ''''this have to be a string variable type'''
    __file_path = "file.json"
    ''''disctionary type object'''
    __objects = {}

    def all(self):
        '''returns objects'''
        return self.__objects

    def new(self, obj):
        '''method to set new object in __object vriable'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''method save'''
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            __dic = {k: v.to_dict() for k, v in self.__objects.items()}
            '''Si no chequea bien hay que hacer sort al JSON'''
            json.dump(__dic, my_file, indent=4, default=str)
            ''' for k, v in __mydic.items():
                print("{}".format(k))
                print("VALUE {}".format(v))'''

    def reload(self):
        '''Reload method'''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as my_file:
                dic_to_dic = json.load(my_file)
                for val in dic_to_dic.values():
                    clsName = val['__class__']
                    self.new(eval(clsName)(**val))
