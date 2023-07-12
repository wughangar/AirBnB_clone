#!/usr/bin/python3
"""
BaseModel
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        public instance attributes initialized.

        Args:
            args: will not be used
            kwargs: dictionary to hold key value args

        Public instances:
            id: assigns id to each instance created within the class using uuid
            created_at: assignes current datetime when an instance was created
            updated_at:assign current datetime
            when instance is created and updated
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # args will not be used

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        string for the exact way the values should be returned
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        public instance method that updates updated_at with current time
        """
        now = datetime.datetime.now()
        self.updated_at = now.isoformat()

    def to_dict(self):
        """
        method that return a dictionary containing
        all key/values of __dict__ of the instance
        """
        return {'__class__': type(self).__name__, **self.__dict__}
