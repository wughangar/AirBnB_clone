#!/usr/bin/python3
"""
BaseModel
"""

import datetime
from uuid import uuid4
import json
import models.__init__
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
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        # args will not be used

        if kwargs:
            v_args = {
                    key: value
                    for key, value in kwargs.items()
                    if key != '__class__'
                    }
            for key, value in v_args.items():
                setattr(self, key, value)
        if self.id not in storage.all():
            storage.new(self)


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
        storage.save()

    def to_dict(self):
        """
        method that return a dictionary containing
        all key/values of __dict__ of the instance
        """
        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                json_dict[key] = value.isoformat()
            else:
                try:
                    json.dumps(value)
                    json_dict[key] = value
                except TypeError:
                    json_dict[key] = str(value)
        return json_dict
