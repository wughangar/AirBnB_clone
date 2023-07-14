#!/usr/bin/python3
"""
more classes
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    state class that inherits from base model
    public attribute:
        name: empty string
    """
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

