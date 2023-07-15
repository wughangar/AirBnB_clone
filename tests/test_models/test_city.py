import unittest
from models.city import City
from models.base_model import BaseModel

"""
test files for city class
"""

class TestCity(unittest.TestCase):
    """
    edge test cases for City state
    """

    def test_child_class(self):
        """
        test to check if City is a child class of BaseModel
        """
        cls = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute(self):
        """
        test for the existance of its attribute
        """
        cls = City()
        self.assertTrue(hasattr(cls, 'state_id'))
        self.assertTrue(hasattr(cls, 'name'))

    def test_empty_string(self):
        # test case for empty string attribute
        cls = City()
        self.assertEqual(cls.name, "")
        self.assertEqual(cls.state_id, "")

    def test_to_dict(self):
        #test case to convert state class into dictionary
        cls = City()
        state_dict = cls.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_str(self):
        # test case for str method in BaseModel class
        cls = City()
        string = str(cls)
        self.assertIn('[City]', string)

    def test_save(self):
        cls = City()
        orig_time = cls.created_at
        upd_time = cls.updated_at
        cls.save()
        self.assertTrue(orig_time, cls.created_at)
        self.assertTrue(upd_time, cls.updated_at)

if __name__ == '__main__':
    unittest.main()
