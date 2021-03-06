#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""
module used to store data
"""


class FileStorage:
    """
        class for serialization and deserialization of classes
    """
    def __init__(self):
        """
        __init__ init the constructor
        """
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        """
            returns objects palce in __objects function
        """

        return self.__objects

    def new(self, obj):
        """
            method to set new object in __object vriable
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            method save to a json file in pathname
        """

        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            __dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(__dic, my_file, indent=4, default=str, sort_keys=True)

    def reload(self):
        """
            Reload method thar reload from the json file
        """
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, mode="r", encoding="utf-8") as mfy:
                    dic_to_dic = json.load(mfy)
                    for val in dic_to_dic.values():
                        clsName = val['__class__']
                        self.new(eval(clsName)(**val))
            else:
                return
        except NoFoundFile:
            pass
