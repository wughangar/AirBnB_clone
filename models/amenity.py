#!/usr/bin/python3

"""
city class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    city class that inherits from Baseclass
    public attributes:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initializatioon of args and kwargs

        Args:
            args: not to be used
            kwargs: keyword arguements
        """
        super().__init__(*args, **kwargs)
