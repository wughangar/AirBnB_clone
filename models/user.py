#!/usr/bin/python3
"""
8. First User
"""

from base_model import BaseModel

class User(BaseModel):
    """
    user class that inherits from BaseClass with the following attributes
    email: user email
    password: user password
    first_name:  user fisrt name
    last_name: user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
