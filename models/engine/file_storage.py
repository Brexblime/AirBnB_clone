#!/usr/bin/python3
"""
file storage
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """filestorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """add new oject"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save object"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """convert object"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
