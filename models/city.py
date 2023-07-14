#!/usr/bin/python3

"""
city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    city class that inherits from Baseclass
    public attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initializatioon of args and kwargs

        Args:
            args: not to be used
            kwargs: keyword arguements
        """
        super().__init__(*args, **kwargs)
