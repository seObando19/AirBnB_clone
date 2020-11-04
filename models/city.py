#!/usr/bin/python3
'''city class for hBnB'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City inherits from Basemodel'''
    state_id = ""
    name = ""
