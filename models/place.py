#!/usr/bin/python3
"""
class place in the site qhere people is
staying
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ place inherits from BaseModel and refers to the site where
    people is staying"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
