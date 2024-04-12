
class User:
    """Represents a user in the library system.

    Attributes:
        name (str): The name of the user.
        user_id (str): The unique ID of the user.
    """
    def __init__(self, name, user_id):
        """Initializes a new User object.

        Args:
            name (str): The name of the user.
            user_id (str): The unique ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """Returns a string representation of the User object."""
        return f"Name: {self.name}\nUser ID: {self.user_id}"
    
    def to_dict(self):
        """Converts the User object to a dictionary."""
        return {
            "name": self.name,
            "user_id": self.user_id
        }

def create_user(users):
    """Creates a new User object based on user input.

    Args:
        users (list): A list of User objects representing the library's users.

    Returns:
        User: The newly created User object.
    """
    while True:
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")

        # Check if the user ID already exists
        if any(user.user_id == user_id for user in users):
            print("User ID already exists. Please enter a different user ID.")
        else:
            return User(name, user_id)

def update_user(users, user_id):
    """Updates a user's information.

    Args:
        users (list): A list of User objects representing the library's users.
        user_id (str): The ID of the user to update.
    """
    for i, user in enumerate(users):
        if user.user_id == user_id:
            new_name = input("Enter new name (or leave blank to keep existing): ")
            if new_name:
                users[i].name = new_name

            new_user_id = input("Enter new user ID (or leave blank to keep existing): ")
            if new_user_id:
                users[i].user_id = new_user_id

            print("User updated successfully.")
            return  
    print("User with ID", user_id, "not found.")

def delete_user_by_id(users, user_id):
    """Deletes a user from the library's system.

    Args:
        users (list): A list of User objects representing the library's users.
        user_id (str): The ID of the user to delete.
    """
    for i, user in enumerate(users):
        if user.user_id == user_id:
            del users[i]
            print("User deleted successfully.")
            return
    print("User with ID", user_id, "not found.")

def list_users(users):
    """Lists all users in the library's system.

    Args:
        users (list): A list of User objects representing the library's users.
    """
    if not users:
        print("No users found.")
    else:
        for user in users:
            print("---------------------------")
            print(user)
            print("---------------------------")
