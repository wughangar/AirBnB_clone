#!/usr/bin/python3
"""
place class that inherits from baseclass
"""

from base_model import BaseModel

class Place(BaseModel):
    """
    place class with the following public attributes

    Public attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list:
    """
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

    def __init__(self, *args, **kwargs):
        """
        initialize args and kwargs

        args:
            args: will not be used
            kwargs: will store keyword args
        """
        super().__init__(*args, **kwargs)
