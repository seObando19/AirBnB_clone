#!/usr/bin/python3
"""
class review
"""


from models.base_model import BaseModel, time_conversor
from datetime import datetime


class Review(BaseModel):
    """ class review
    """
    place_id = ""
    user_id = ""
    text = ""
