import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

"""
test cases for File Storage class
"""

class FileStorageTestCase(unittest.TestCase):
    """
    File storage test cases
    """

    def test_all(self):
        # testing the all method - all()
        # adding some objects to storage
        cls = FileStorage()
        obj1 = BaseModel()
        obj2 = User()
        cls.new(obj1)
        cls.new(obj2)
        # check if all() return a dictionary of objects
        self.assertIsInstance(cls.all(), dict)

    def test_save_and_reload(self):
        # testing save and reload methods: save(), reload()
        # adding some objects to the storage
        cls = FileStorage()
        obj1 = BaseModel()
        obj2 = User()
        cls.new(obj1)
        cls.new(obj2)
        # save the objects in new file by calling save 
        cls.save()
        # clearing the storage
        cls = None
        # reloading objects from the file
        cls = FileStorage()
        cls.reload()
        # check if objects are reloaded
        self.assertIsInstance(cls.all(), dict)

if __name__ == '__main_':
    unittest.main()

