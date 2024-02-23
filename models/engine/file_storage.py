#!/usr/bin/python3
'''
    Module containing class FileStorage.
'''
import json


class FileStorage:
    '''
    FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        ''': returns the dictionary __objects'''
        if cls:
            dictionary = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    dictionary[key] = value
            return dictionary
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id.'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        objects = {}
        for key, value in self.__objects.items():
            objects[key] = value.to_dict()
        jsondump = json.dumps(objects)
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as jsonfile:
                jsonfile.write(jsondump)
        except IOError:
            print("Error Writing to file")

    def reload(self):
        from os import path
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classes = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as jsonfile:
                dicts = json.load(jsonfile)
            for key, value in dicts.items():
                class_name = value["__class__"]
                if class_name in classes:
                    obj = eval(f"{class_name}(**{value})")
                self.__objects[key] = obj
            self.save()

    def delete(self, obj=None):
        """
        To delete obj from __objects if it’s inside - if obj is equal to None,
        the method should not do anything
        """
        if obj is not None:
            del self.__objects[f"{obj.__class__.__name__}.{obj.id}"]