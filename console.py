#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
import json
import shlex
from models import storage
from models import classes
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
        Contains the entry point of the command interpreter.
    '''

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        '''
            Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        '''
            Exits after receiving the EOF signal.
        '''
        return True

    def do_create(self, args):
        '''
            Create a new instance of class BaseModel and saves it
            to the JSON file.
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args, posix=False)
            new_instance = eval(args[0])()
            ''' filter the dict '''
#            print("about to enter for loop")
            for arg in range(len(args)):
#                print("for iteration - arg: {}".format(arg))
                if '=' in args[arg]:
#                    print("DEBUG: entered if")
                    key, value = args[arg].split('=')
#                    print("DEBUG: value[0]={}".format(value[0]))
                    if value[0] == "\"" and value[len(value) - 1] == value[0]:
#                        print("DEBUG: 1")
                        value = value[1:len(value) - 1]
                        value = value.replace("_", " ")
                        for idx in range(len(value)):
                            if value[idx] == "\"":
                                value = value[:idx] + "\\" + value[idx:]
                    elif '.' in value:
#                        print("DEBUG: 2")
                        value = float(value)
                    elif value.isdigit():
#                        print("DEBUG: 3")
                        value = int(value)
                    else:
#                        print("DEBUG: 4")
                        continue
#                    print("about to set attr")
#                    print("key: {}".format(key))
#                    print("val: {}".format(value))
#                    print("DEBUG - type of value: {}".format(type(value)))
                    setattr(new_instance, key, value)
 #                   print("we set da attr")
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")
        
    def do_show(self, args):
        '''
            Print the string representation of an instance baed on
            the class name and id given as args.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all(args[0])
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        '''
            Deletes an instance based on the class name and id.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        '''
            Prints all string representation of all instances
            based or not on the class name.
        '''
        obj_list = []
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 0:
            for key, value in storage.all().items():
                obj_list.append(value)
        else:
            for key, value in storage.all(eval(args)).items():
                obj_list.append(value)
        print(obj_list)

    def do_update(self, args):
        '''
            Update an instance based on the class name and id
            sent as args.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):
        '''
            Prevents printing anything when an empty line is passed.
        '''
        pass

    def do_count(self, args):
        '''
            Counts/retrieves the number of instances.
        '''
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        '''
            Catches all the function names that are not expicitly defined.
        '''
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    '''
        Entry point for the loop.
    '''
    HBNBCommand().cmdloop()
