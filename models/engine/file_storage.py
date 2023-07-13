#!/usr/bin/python3
"""
file storage class
"""
import json

class FileStorage:
    """
    this class serializes and deserializes json files
    """
    def __init__(self):
        """
        initializing public class attributes
        with private attributes; file_path and objects
        Args:
            file_path: string-path to the json file
            objects: dictionary- empty but will store objects by class name.id
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        public instance method

        Returns: a dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """
        public instance method that sets objects to obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        public attribute method that serializes objects to the json file 
        path: __file_path
        """
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        public instance method that deserializes the json file to __objects
        only if the json file to be found using __file_path exists.
        do nothing when it doesnt exist, no exception to be raised
        """
        try:
            with open(self.__file_path, 'r') as file:
                dict_obj = json.load(file)
                for key, value in dict_obj.items():
                    class_name, obj_id = key.split('.')
                    cls = globals().get(class_name)
                    if cls:
                        obj = cls(**value)
                        self.new(obj)
        except FileNotFoundError:
            pass
