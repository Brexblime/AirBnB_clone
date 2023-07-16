#!/usr/bin/python3
"""
file storage
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """filestorage class"""

    CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

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

    def _deserialize_objects(self):
        """Deserialize the JSON file and create User objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                for obj_id in json_dict:
                    class_name = json_dict[obj_id].get("__class__")
                    if class_name == "User":
                        self.__objects[obj_id] = User(**json_dict[obj_id])

    def _serialize_objects(self):
        """Serialize the User objects and save to the JSON file"""
        json_dict = {}
        for obj_id in self.__objects:
            json_dict[obj_id] = self.__objects[obj_id].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)
