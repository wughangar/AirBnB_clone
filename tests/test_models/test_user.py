import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

"""
test cases for class User
"""

class TestUser(unittest.TestCase):
    """
    test case edge cases
    """
    def test_child_class(self):
        """
        test if user is a sub-class of BaseModel
        """
        self.user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_set_attributes(self):
        """
        test for available attributes in user class
        """
        self.user = User()
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_empty_attribute_strings(self):
        """
        test case to test for default empty attribute strings
        """
        self.user = User()
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """
        test case for user to dict
        """
        self.user = User()
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_kwargs(self):
        cls = User()
        cls = User(email="wughangar.rose@gmail.com", password="xyz", first_name="Tony", last_name="mbokola")
        self.assertEqual(cls.email, "wughangar.rose@gmail.com")
        self.assertEqual(cls.password, "xyz")
        self.assertEqual(cls.first_name, "Tony")
        self.assertEqual(cls.last_name, "mbokola")

    def test_main_attributes(self):
        """
        test cases for inherited attributes not empty
        """
        cls = User()
        self.assertIsNotNone(cls.id)
        self.assertIsInstance(cls.created_at, datetime)
        self.assertIsInstance(cls.updated_at, datetime)

    def test_str(self):
        """
        test for str method inherited from basemodel
        """
        cls = User()
        string = str(cls)
        self.assertIn('[User]', string)
        self.assertIn(cls.id, string)

    def test_save(self):
        """
        test save method on class user
        """
        cls = User()
        cls_created_at = cls.created_at
        cls_updated_at = cls.updated_at
        cls.save()
        self.assertNotEqual(cls_created_at, cls.updated_at)

if __name__ == '__main__':
    unittest.main()
