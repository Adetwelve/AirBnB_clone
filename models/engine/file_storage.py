#!/usr/bin/python3
import json
""" 
    Write a class FileStorage that serializes instances \
    to a JSON file and deserializes JSON file to instances:
"""


class FileStorage():
    """
        Representation of class storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            j_file = {k : V.to_dict() for K, v in self.__object.items()}
            json.dump(j_file, f)


