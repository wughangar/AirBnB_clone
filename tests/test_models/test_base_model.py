import unittest
from datetime import datetime
from models.base_model import BaseModel

"""
test cases for the basemodel class
"""


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        test for the correct initialization of attributes
        """
        cls = BaseModel()
        self.assertIsNotNone(cls.id)
        self.assertIsInstance(cls.created_at, datetime)
        self.assertIsInstance(cls.updated_at, datetime)

    def test_str(self):
        """
        test for str to return correct format
        """
        cls = BaseModel()
        string = str(cls)
        self.assertIn('[BaseModel', string)
        self.assertIn(cls.id, string)

    def test_save(self):
        """
        test for the save function to compare time on updated at
        """
        cls = BaseModel()
        last_updated_at = cls.updated_at
        cls.save
        self.assertEqual(cls.updated_at, last_updated_at)

    def test_csave(self):
        """
        test for the save function to comapre created at
        """
        cls = BaseModel()
        last_created_at = cls.created_at
        cls.save
        self.assertEqual(cls.created_at, last_created_at)

    def test_id_save(self):
        """
        test for save mthod to save the id
        """
        cls = BaseModel()
        c_id = cls.id
        cls.save
        self.assertEqual(c_id, cls.id)

    def test_to_dict(self):
        """
        test for to dict method
        """
        cls = BaseModel()
        cls_dict = cls.to_dict()
        self.assertIsInstance(cls_dict, dict)


if __name__ == '__main__':
    unittest.main()
