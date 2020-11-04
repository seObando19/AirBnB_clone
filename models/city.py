#!/usr/bin/python3
'''city class for hBnB and refers to
the city placed'''


from models.base_model import BaseModel


class City(BaseModel):
    '''City inherits from Basemodel and refers to
    teh city placed'''

    state_id = ""
    name = ""
