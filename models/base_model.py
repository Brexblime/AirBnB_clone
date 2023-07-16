#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Initializing"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str"""

        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """saving"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return (data)
