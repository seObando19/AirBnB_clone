#!/usr/bin/python3
'''this module is the base class for all other classes'''
from uuid import uuid4
from datetime import datetime, date, time

class BaseModel:
    '''Base Model class for the proyect'''
    def __init__(self, *args, **kwargs):
        dt = datetime.now()

        self.id = str(uuid4())
        """
        dt.strftime("%Y-%m-%dT%H:%M:%S.%f")
        """
        self.created_at = dt
        self.updated_at = dt

    def __str__(self):
        ''''''
        text = "[{}] ({}) {}"
        return text.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        dt = datetime.now()

        self.updated_at = dt

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        '''
        self.__dict__.update(
            {"updated_at" : self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")}
            )
        self.__dict__.update(
            {"created_at" : self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")}
        )
        self.__dict__['__class__'] = self.__class__.__name__
        return dict(self.__dict__)