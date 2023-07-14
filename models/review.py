#!/usr/bin/python3
"""
review class that inherits from BaseModel
"""

from base_model import BaseModel


class Review(BaseModel):
    """
    child class with the following public class attributes

    public attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        initialize args and kwargs

           args: will not be used
           kwargs: kwayword args
        """
        super().__init__(*args, **kwargs)
