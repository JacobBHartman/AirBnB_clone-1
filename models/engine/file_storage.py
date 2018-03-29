#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        print("DEBUG: Does consoloe.do_all() take us here?")
        if cls != None:
            print("entered IF")
            objs_of_one_class = {}
            for key, value in self.__objects.items():
                if cls == type(value):
                    objs_of_one_class[key] = value
            print("\nDEBUG: {}\n".format(objs_of_one_class))
            return objs_of_one_class
        else:
            print("entered ELSE")
            return self.__objects
        print("entereed NEITHER")

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        self.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                self.__objects = json.load(fd)
            for key, val in self.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                self.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Public instance method to delete an object from __objects if there
        :param obj: The object to be deleted
        """
        if obj is None:
            return
        else:
            key = obj.__class__.__name__ + "." + obj.id
            del(self.__objects[key])
