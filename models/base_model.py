#!/usr/bin/python3

import uuid
from datetime import datetime

import models
"""
Module includes the BaseModel
defines all common attributes/methods for other classes
"""

class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Initialize public instances"""

        if kwargs:
              for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """
        Return string of info about model
        in the form of: [<class name>] (<self.id>) <self.__dict__>
        """
        form = '[{}] ({}) ()'
        return (form.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Update instance with updated time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary of all keys/values of __dict__ of the instance
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = str(value.isoformat())
            else:
                dic[key] = value
        return (dic)
