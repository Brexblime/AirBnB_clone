#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import models
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return (True)

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached"""
        return (True)

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = models.classes[arg]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + '.' + instance_id
                print(models.storage.all()[key])
            except IndexError:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + '.' + instance_id
                all_objects = models.storage.all()
                if key in all_objects:
                    del all_objects[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representation of all instances"""
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                class_name = args[0]
                print([str(obj) for obj in objects.values() if type(obj).__name__ == class_name])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + '.' + instance_id
                all_objects = models.storage.all()
                if key not in all_objects:
                    print("** no instance found **")
                    return
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return
                attribute_name = args[2]
                attribute_value = args[3].strip('\"')
                obj = all_objects[key]
                setattr(obj, attribute_name, attribute_value)
                obj.save()
            except IndexError:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
