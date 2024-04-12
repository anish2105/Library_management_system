import json
from book import Book
from user import User

def save_data(books, users):
    """Saves the library data to a JSON file.

    Args:
        books (list): A list of Book objects representing the library's collection.
        users (list): A list of User objects representing the library's users.
    """
    data = {
        "books": [book.__dict__ for book in books],
        "users": [user.to_dict() for user in users]
    }
    with open("library_data.json", "w") as file:
        json.dump(data, file)

def load_data():
    """Loads the library data from a JSON file.

    Returns:
        tuple: A tuple containing two lists - the list of Book objects and the list of User objects.
    """
    try:
        with open("library_data.json", "r") as file:
            data = json.load(file)
            books_data = data.get("books", [])
            users_data = data.get("users", [])
            
            books = [Book(book['title'], book['author'], book['isbn'], book['available'], book['borrower_id']) for book in books_data]
            users = [User(user['name'], user['user_id']) for user in users_data]
            
            return books, users
    except FileNotFoundError:
        return [], []
