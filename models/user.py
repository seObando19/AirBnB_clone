#!/usr/bin/python3
"""user class for those that uses the app
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ User is a class refered to
    who is using it """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
