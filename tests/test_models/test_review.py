import unittest
from models.review import Review
from models.base_model import BaseModel

"""
test files for review class
"""

class TestReview(unittest.TestCase):
    """
    edge test cases for class Review
    """

    def test_child_class(self):
        """
        test to check if Review is a child class of BaseModel
        """
        cls = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attribute(self):
        """
        test for the existance of its attribute
        """
        cls = Review()
        self.assertTrue(hasattr(cls, 'place_id'))
        self.assertTrue(hasattr(cls, 'user_id'))
        self.assertTrue(hasattr(cls, 'text'))

    def test_empty_string(self):
        # test case for empty string attribute
        cls = Review()
        self.assertEqual(cls.place_id, "")
        self.assertEqual(cls.user_id, "")
        self.assertEqual(cls.text, "")

    def test_to_dict(self):
        #test case to convert Review class into dictionary
        cls = Review()
        state_dict = cls.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_str(self):
        # test case for str method in BaseModel class
        cls = Review()
        string = str(cls)
        self.assertIn('[Review]', string)

    def test_save(self):
        cls = Review()
        orig_time = cls.created_at
        upd_time = cls.updated_at
        cls.save()
        self.assertTrue(orig_time, cls.created_at)
        self.assertTrue(upd_time, cls.updated_at)

if __name__ == '__main__':
    unittest.main()
