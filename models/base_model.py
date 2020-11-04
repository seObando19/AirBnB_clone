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
        ''' initializes the class BaseModel '''
        if kwargs:
            self.created_at = time_conversor(kwargs["created_at"])
            self.updated_at = time_conversor(kwargs["updated_at"])
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today().isoformat()
            self.updated_at = datetime.today().isoformat()
            models.storage.new(self)

    def __str__(self):
        """
           String representation of BaseModel class
        """
        self.__dict__.update({
            "created_at": time_conversor(self.created_at),
            "updated_at": time_conversor(self.updated_at),
        })
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__
            of the instance
        """
        if type(self.created_at) in [str]:
            self.created_at = time_conversor(self.created_at)
        if type(self.updated_at) in [str]:
            self.updated_at = time_conversor(self.updated_at)
        self.created_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictionary = (self.__dict__).copy()
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
