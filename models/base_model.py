#!/usr/bin/python3
'''this module is the base class for all other classes'''
from uuid import uuid4
from datetime import datetime

class BaseModel:
    '''Base Model class for the proyect'''
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid4())
        self.created_at = datetime.today().isoformat()
        self.updated_at = datetime.today().isoformat()

    def __str__(self):
        ''''''
        text = "[{}] ({}) {}"
        return text.format(__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''