#!/usr/bin/python3
"""
class review is calification of the stance in the place
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ class review
    """

    place_id = ""
    user_id = ""
    text = ""
