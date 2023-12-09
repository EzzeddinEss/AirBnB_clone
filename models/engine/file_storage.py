#!/usr/bin/python3
"""
FileStorage module
"""


import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class is responsible for storing & retrieving objects in a JSON file.
    It provides methods for managing objects, saving them to the file,
    and reloading them from the file.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the FileStorage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the FileStorage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves all objects in the FileStorage to the JSON file.
        """
        py_obj = {}
        for key, val in FileStorage.__objects.items():
            py_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as file:
            json.dump(py_obj, file)

    def reload(self):
        """
        Reloads objects from the JSON file into the FileStorage.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                deserialized_file = json.load(file)
                for key, val in deserialized_file.items():
                    clss_name = val["__class__"]
                    obj = eval(clss_name)(**val)
                    FileStorage.__objects[key] = obj
        else:
            pass
