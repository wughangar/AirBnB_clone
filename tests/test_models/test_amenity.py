import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

"""
test files for state class
"""

class TestState(unittest.TestCase):
    """
    edge test cases for class state
    """

    def test_child_class(self):
        """
        test to check if state is a child class of BaseModel
        """
        cls = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute(self):
        """
        test for the existance of its attribute
        """
        cls = Amenity()
        self.assertTrue(hasattr(cls, 'name'))

    def test_empty_string(self):
        # test case for empty string attribute
        cls = Amenity()
        self.assertEqual(cls.name, "")

    def test_to_dict(self):
        #test case to convert  class into dictionary
        cls = Amenity()
        cls_dict = cls.to_dict()
        self.assertIsInstance(cls_dict, dict)

    def test_str(self):
        # test case for str method in BaseModel class
        cls = Amenity()
        string = str(cls)
        self.assertIn('[Amenity]', string)

    def test_save(self):
        """
        test for save of created at and updated at for Amenity class
        """
        cls = Amenity()
        orig_time = cls.created_at
        upd_time = cls.updated_at
        cls.save()
        self.assertEqual(orig_time, cls.created_at)
        self.assertNotEqual(upd_time, cls.updated_at)

if __name__ == '__main__':
    unittest.main()
