#!/usr/bin/python3
'''state class for hBnB and it refers to the state qhere
city is located'''


from models.base_model import BaseModel


class State(BaseModel):
    '''state inherits from BaseModel'''

    name = ""
