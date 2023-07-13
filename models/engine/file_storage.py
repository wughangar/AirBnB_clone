#!/usr/bin/python3
import json


class FileStorage:
    """
    this class serializes and deserializes json files
    """
    def __init__(self):
        """
        initializing private class attributes
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
        public instance method that sets objects to obj with key
        <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        public attribute method that serializes objects to the json file
        path: __file_path
        """
        with open(self.__file_path, 'w') as json_file:
            dic = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(dic, json_file)

    def reload(self):
        """
        public instance method that deserializes the json file to __objects
        only if the json file to be found using __file_path exists.
        do nothing when it doesnt exist, no exception to be raised
        """
        try:
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
