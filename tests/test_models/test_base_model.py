#!/usr/bin/python3
"""defines unittestsfor models/base_model.py."""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel class"""

    def test_attributes(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

        def test_str(self):
            obj = BaseModel()
            obj.name = "My First Model"
            obj.my_number = 89
            expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
            self.assertEqual(str(obj), expected_str)

        def test_save(self):
            obj = BaseModel()
            original_updated_at = obj.updated_at
            obj.save()
            self.assertNotEqual(obj.updated_at, original_updated_at)

        def test_to_dict(self):
            obj = BaseModel()
            obj.name = "My First Model"
            obj.my_number = 89
            data = obj.to_dict()
            self.assertEqual(data['name'], "My First Model")
            self.assertEqual(data['my_number'], 89)
            self.assertEqual(data['__class__'], "BaseModel")
            self.assertEqual(data['created_at'], obj.created_at.isoformat())
            self.assertEqual(data['updated_at'], obj.updated_at.isoformat())

class TestBaseModelDict(unittest.TestCase):
    """basemodeldict class"""

    def test_from_dict(self):
        """define test_from_dict"""

        obj = BaseModel()
        obj.name = "My_First_Model"
        obj.my_number = 89
        obj_json = obj.to_dict()

        new_obj = BaseModel(**obj_json)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)
        self.assertEqual(obj.name, new_obj.name)
        self.assertEqual(obj.my_number, new_obj.my_number)
        self.assertEqual(str(obj), str(new_obj))

if __name__ == '__main__':
    unittest.main()
