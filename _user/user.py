"""
This class handles the user data and operations.

Attributes:
    # user_id (int): The unique id of the user.
    # DATABASE (str): The path of the user database file.
    # __users (list): The list of users.

Methods:
    load_users: Reads the user data from the database file.
    save_users: Writes the user data to the database file.
    create_user: Adds a new user to the database.
    edit_user: Edits an existing user in the database.
    delete_user: Deletes an existing user from the database.
    __str__: Returns a string representation of the user object.
"""

import json
import os
from verification import *


class User:
    user_id = 0
    DATABASE = os.path.join(os.path.dirname(__file__), '..', 'database', 'user_db.json')

    def __init__(self, username=None, fullname=None, email=None, password=None):
        """
            To Do: accept creating of users in bulk and change the way the parameters are being passed
            ie instead of passing the username, fullname, email, and password as parameters in the __init__ method,
            pass them directly to the create_user and edit_user methods.
        
        """
        self.__users = self.load_users()  # Load users from JSON file
        self.__username = username.strip() if username else None
        self.__fullname = fullname
        self.__email = email.strip() if email else None
        self.__password = password.strip() if password else None

    @staticmethod
    def load_users():
        """
        Reads the user data from the database file.

        Returns:
            list: The list of users.
        """
        try:
            with open(User.DATABASE, 'r') as file:
                data = json.load(file)
                # Check if data is empty, if so, return an empty dictionary
                if not data:
                    return {}
                return data
        except FileNotFoundError:
            return {}  # Return an empty dictionary if file doesn't exist
        except json.JSONDecodeError:
            return {}  # Return an empty dictionary if JSON decoding fails

    def save_users(self):
        """
        Writes the user data to the database file.
        """
        with open(self.DATABASE, 'w') as file:
            json.dump(self.__users, file, indent=4)

    def create_user(self):
        """
        Adds a new user to the database.

        Returns:
            dict: A dictionary containing the response message and status code.
        """
        # Check if username, email, and password fields are present
        if not all([self.__username, self.__email, self.__password]):
            return {'Error': 'Username, email, and password fields are required', 'status': '400'}

        # Check if email address is valid
        if not email_verification(self.__email):
            return {'Error': 'Invalid email address', 'status': '400'}

        # Check if password meets requirements
        if not password_verification(self.__password):
            return {'Error': 'Password does not meet password requirement', 'status': '400'}

        # initialize the last user id variable
        last_user_id = None

        # Check if username already exists
        for user_id, user_data in self.__users.items():
            if user_data['username'] == self.__username:
                return {'Error': 'User with this username already exists', 'status': '400'}

            if user_data['email'] == self.__email:
                return {'Error': 'User with this email already exists', 'status': '400'}

            # Set last_user_id to the current user_id in the loop
            last_user_id = int(user_id)

        # Use the last_user_id obtained from the loop
        if last_user_id is not None:
            user_id = last_user_id + 1
        else:
            # If there are no existing users, start user_id from 1
            user_id = 1

        # Create new user object
        new_user = {
            'id': user_id,
            'username': self.__username,
            'fullname': self.__fullname,
            'email': self.__email,
            'password': self.__password
        }

        # Add new user to the database
        self.__users[user_id] = new_user
        self.save_users()

        # Return success message
        return {'Success': 'User created successfully', 'status': '200', 'user': new_user}

    def edit_user(self, user_id):
        """
        Edits an existing user in the database.

        Args:
            user_id (int): The id of the user to edit.

        Returns:
            dict: A dictionary containing the response message and status code.
        """
        # Check if the user exists
        user = next((user_data for u, user_data in self.__users.items() if user_data['id'] == user_id), None)

        if not user:
            return {'Error': 'User not found', 'status': '404'}

        # Validate email and password if provided
        if self.__email and not email_verification(self.__email):
            return {'Error': 'Invalid email address', 'status': '400'}

        if self.__password and not password_verification(self.__password):
            return {'Error': 'Password does not meet password requirement', 'status': '400'}

        # Check for changes
        if (self.__username is not None and self.__username != user['username']) or \
                (self.__fullname is not None and self.__fullname != user['fullname']) or \
                (self.__email is not None and self.__email != user['email']) or \
                (self.__password is not None and self.__password != user['password']):

            # Check if username already exists
            for user_id, user_data in self.__users.items():
                if user_data['username'] == self.__username:
                    return {'Error': 'User with this username already exists', 'status': '400'}

                if user_data['email'] == self.__email:
                    return {'Error': 'User with this email already exists', 'status': '400'}

            # Changes were made, update user and save
            if self.__username:
                user['username'] = self.__username
            if self.__fullname:
                user['fullname'] = self.__fullname
            if self.__email:
                user['email'] = self.__email
            if self.__password:
                user['password'] = self.__password

            self.save_users()
            return {'Success': 'User updated successfully', 'status': '200', 'user': user}

        # No changes detected
        return {'Error': 'No changes made', 'status': '400'}

    def delete_user(self, user_id):
        """
        Deletes an existing user from the database.

        Args:
            user_id (int, optional): The id of the user to delete. If not provided,
                all users will be deleted.

        Returns:
            dict: A dictionary containing the response message and status code.
        """
        # Check if the user exists
        for key, value in self.__users.items():
            if value['id'] == user_id:
                # Delete the user from the users dictionary
                del self.__users[key]
                self.save_users()  # Save updated user data to JSON file
                return {'Success': 'User deleted successfully', 'status': '200'}

        return {'Error': 'User not found', 'status': '404'}

    def __len__(self):
        return len(self.__users)

    def __str__(self):
        """
        Returns a string representation of the user object.

        Returns:
            str: The string representation of the user object.
        """
        return str(self.__users) + '\nstatus: 200'
