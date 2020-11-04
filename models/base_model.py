#!/usr/bin/python3
"""
Define  BaseModel class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
        Base Model class for the proyect
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = time_conversor(kwargs["created_at"])
            if "updated_at" in kwargs:
                kwargs["updated_at"] = time_conversor(kwargs["updated_at"])
            for key in kwargs.keys():
                if key is '__class__':
                    continue
                    (self.__dict__)[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today().isoformat()
            self.updated_at = datetime.today().isoformat()
            models.storage.new(self)

    def __str__(self):
        """
           String representation of BaseModel class
        """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__
            of the instance
        """
        dictionary = (self.__dict__).copy()
        if "created_at" in dictionary:
            self.created_at = time_conversor(self.created_at)
        if "updated_at" in dictionary:
            self.updated_at = time_conversor(self.updated_at)
        dictionary['__class__'] = self.__class__.__name__
        return dictionary


def time_conversor(obj):
    """
        Define time conversor
        that return new time object
    """
    if type(obj) in [datetime]:
        obj = obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S.%f")
