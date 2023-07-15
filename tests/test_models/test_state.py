import unittest
from models.state import State
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
        cls = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_attribute(self):
        """
        test for the existance of its attribute
        """
        cls = State()
        self.assertTrue(hasattr(cls, 'name'))

    def test_empty_string(self):
        # test case for empty string attribute
        cls = State()
        self.assertEqual(cls.name, "")

    def test_to_dict(self):
        #test case to convert state class into dictionary
        cls = State()
        state_dict = cls.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_str(self):
        # test case for str method in BaseModel class
        cls = State()
        string = str(cls)
        self.assertIn('[State]', string)

    def test_save(self):
        cls = State()
        orig_time = cls.created_at
        upd_time = cls.updated_at
        cls.save()
        self.assertTrue(orig_time, cls.created_at)
        self.assertTrue(upd_time, cls.updated_at)
if __name__ == '__main__':
    unittest.main()
