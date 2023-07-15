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

