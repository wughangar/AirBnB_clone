import unittest
from models.place import Place
from models.base_model import BaseModel


"""
test files for Place class
"""


class TestPlace(unittest.TestCase):
    """
    edge test cases for class Place
    """

    def test_child_class(self):
        """
        test to check if Place is a child class of BaseModel
        """
        cls = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attribute(self):
        """
        test for the existance of its attribute
        """
        cls = Place()
        self.assertTrue(hasattr(cls, 'latitude'))
        self.assertTrue(hasattr(cls, 'city_id'))
        self.assertTrue(hasattr(cls, 'user_id'))
        self.assertTrue(hasattr(cls, 'name'))
        self.assertTrue(hasattr(cls, 'description'))
        self.assertTrue(hasattr(cls, 'number_rooms'))
        self.assertTrue(hasattr(cls, 'number_bathrooms'))
        self.assertTrue(hasattr(cls, 'max_guest'))
        self.assertTrue(hasattr(cls, 'price_by_night'))
        self.assertTrue(hasattr(cls, 'longitude'))
        self.assertTrue(hasattr(cls, 'amenity_ids'))

    def test_empty_string(self):
        # test case for empty string attribute
        cls = Place()
        self.assertEqual(cls.city_id, "")
        self.assertEqual(cls.user_id, "")
        self.assertEqual(cls.name, "")
        self.assertEqual(cls.description, "")
        self.assertEqual(cls.number_rooms, 0)
        self.assertEqual(cls.number_bathrooms, 0)
        self.assertEqual(cls.max_guest, 0)
        self.assertEqual(cls.price_by_night, 0)
        self.assertEqual(cls.latitude, 0.0)
        self.assertEqual(cls.longitude, 0.0)
        self.assertEqual(cls.amenity_ids, "")

    def test_to_dict(self):
        # test case to convert Place class into dictionary
        cls = Place()
        state_dict = cls.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_str(self):
        # test case for str method in BaseModel class
        cls = Place()
        string = str(cls)
        self.assertIn('[Place]', string)

    def test_save(self):
        # test case for if these methods are corectly created and saved
        cls = Place()
        orig_time = cls.created_at
        upd_time = cls.updated_at
        cls.save()
        self.assertTrue(orig_time, cls.created_at)
        self.assertTrue(upd_time, cls.updated_at)


if __name__ == '__main__':
    unittest.main()
