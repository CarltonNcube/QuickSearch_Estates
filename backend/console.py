#!/usr/bin/python3
"""Console for QuickSearch Estates - Buying and Selling Properties"""

import cmd
import requests
from sqlalchemy.orm import sessionmaker
from models.engine.fileStorage import FileStorage
from models.engine.DBStorage import DBStorage
from models.models import Base, engine, User, City, County, Province, State, Continent, Suburb, Property, Review, Amenity, Place, Preference

# Define the classes dictionary
classes = {
    "User": User,
    "City": City,
    "County": County,
    "Province": Province,
    "State": State,
    "Continent": Continent,
    "Suburb": Suburb,
    "Property": Property,
    "Review": Review,
    "Amenity": Amenity,
    "Place": Place,
    "Preference": Preference
}

# Create session
Session = sessionmaker(bind=engine)
db_session = Session()

class QuickSearchConsole(cmd.Cmd):
    """Command-line interface for QuickSearch Estates - Buying and Selling Properties"""

    prompt = '(quicksearch) '

    def do_EOF(self, arg):
        """Exit the console"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def default(self, line):
        """Handle default command"""
        args = line.split()
        if len(args) == 0:
            print("*** Unknown syntax: missing command ***")
            return
        class_name = args[0]
        if class_name not in classes:
            print("*** Unknown syntax: invalid class name ***")
            return
        if len(args) > 1:
            if args[1] == "all":
                self.do_all(class_name)
                return
            elif args[1] == "show" and len(args) > 2:
                instance_id = args[2]
                self.do_show(f"{class_name} {instance_id}")
                return
            elif args[1] == "destroy" and len(args) > 2:
                instance_id = args[2]
                self.do_destroy(f"{class_name} {instance_id}")
                return
            elif args[1] == "update" and len(args) > 2:
                instance_id = args[2]
                attribute = args[3]
                value = args[4]
                self.do_update(f"{class_name} {instance_id} {attribute} {value}")
                return
        print("*** Unknown syntax: invalid command ***")

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("*** Missing class name ***")
            return
        class_name = args[0]
        if class_name not in classes:
            print("*** Unknown class name ***")
            return
        Model = classes[class_name]
        instance = Model()
        db_session.add(instance)
        db_session.commit()
        print(f"New {class_name} created with ID: {instance.id}")

    def do_show(self, arg):
        """Show details of an instance"""
        args = arg.split()
        if len(args) != 2:
            print("*** Usage: show <class name> <instance id> ***")
            return
        class_name, instance_id = args
        Model = classes[class_name]
        instance = db_session.query(Model).filter_by(id=instance_id).first()
        if not instance:
            print("*** No instance found ***")
            return
        print(instance)

    def do_all(self, arg):
        """Show all instances of a class"""
        class_name = arg
        if class_name not in classes:
            print("*** Unknown class name ***")
            return
        Model = classes[class_name]
        instances = db_session.query(Model).all()
        print([str(instance) for instance in instances])

    def do_destroy(self, arg):
        """Delete an instance"""
        args = arg.split()
        if len(args) != 2:
            print("*** Usage: destroy <class name> <instance id> ***")
            return
        class_name, instance_id = args
        Model = classes[class_name]
        instance = db_session.query(Model).filter_by(id=instance_id).first()
        if not instance:
            print("*** No instance found ***")
            return
        db_session.delete(instance)
        db_session.commit()
        print(f"{class_name} instance {instance_id} deleted successfully")

    def do_update(self, arg):
        """Update an instance attribute"""
        args = arg.split()
        if len(args) < 4:
            print("*** Usage: update <class name> <instance id> <attribute> <value> ***")
            return
        class_name, instance_id, attribute = args[:3]
        value = " ".join(args[3:])
        Model = classes[class_name]
        instance = db_session.query(Model).filter_by(id=instance_id).first()
        if not instance:
            print("*** No instance found ***")
            return
        setattr(instance, attribute, value)
        db_session.commit()
        print(f"{attribute} updated successfully for {class_name} instance {instance_id}")

    # Function to create a new user via HTTP POST request
    def create_user(self, name, email):
        user_data = {
            "name": name,
            "email": email
        }
        response = requests.post('http://localhost:5000/api/users', json=user_data)
        if response.status_code == 201:
            return response.json()
        else:
            return f"Failed to create user: {response.text}"

    # Function to retrieve all users via HTTP GET request
    def get_all_users(self):
        response = requests.get('http://localhost:5000/api/users')
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to get users: {response.text}"

    # Function to retrieve a user by ID via HTTP GET request
    def get_user_by_id(self, user_id):
        response = requests.get(f'http://localhost:5000/api/users/{user_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to get user: {response.text}"

    # Function to update a user by ID via HTTP PUT request
    def update_user(self, user_id, updated_data):
        response = requests.put(f'http://localhost:5000/api/users/{user_id}', json=updated_data)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to update user: {response.text}"

    # Function to delete a user by ID via HTTP DELETE request
    def delete_user(self, user_id):
        response = requests.delete(f'http://localhost:5000/api/users/{user_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to delete user: {response.text}"

if __name__ == '__main__':
    QuickSearchConsole().cmdloop()

