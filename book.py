
class Book:
    """Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        available (bool): Indicates whether the book is available for borrowing.
        borrower_id (str): The ID of the user who borrowed the book.
    """

    def __init__(self, title, author, isbn, available=True, borrower_id=None):
        """Initializes a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            available (bool, optional): Indicates whether the book is available for borrowing. Defaults to True.
            borrower_id (str, optional): The ID of the user who borrowed the book. Defaults to None.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.borrower_id = borrower_id

    def __str__(self):
        """Returns a string representation of the Book object."""
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailable: {'Yes' if self.available else 'No'}\nBorrower ID: {self.borrower_id}"

def create_book(books):
    """Creates a new Book object based on user input.

    Args:
        books (list): A list of Book objects representing the library's collection.

    Returns:
        Book: The newly created Book object.
    """
    while True:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")

        # Check if the ISBN already exists
        if any(book.isbn == isbn for book in books):
            print("ISBN already exists. Please enter a different ISBN.")
        else:
            return Book(title, author, isbn)

def update_book(books, isbn):
    """Updates a book's information.

    Args:
        books (list): A list of Book objects representing the library's collection.
        isbn (str): The ISBN of the book to update.
    """
    for i, book in enumerate(books):
        if book.isbn == isbn:
            new_title = input("Enter new title (or leave blank to keep existing): ")
            if new_title:
                books[i].title = new_title

            new_author = input("Enter new author (or leave blank to keep existing): ")
            if new_author:
                books[i].author = new_author

            new_isbn = input("Enter new ISBN (or leave blank to keep existing): ")
            if new_isbn:
                books[i].isbn = new_isbn

            print("Book updated successfully.")
            return  # Exit after successful update
    print("Book with ISBN", isbn, "not found.")

def delete_book_by_isbn(books, isbn):
    """Deletes a book from the library's collection.

    Args:
        books (list): A list of Book objects representing the library's collection.
        isbn (str): The ISBN of the book to delete.
    """
    for i, book in enumerate(books):
        if book.isbn == isbn:
            del books[i]
            print("Book deleted successfully.")
            return
    print("Book with ISBN", isbn, "not found.")

def list_books(books):
    """Lists all books in the library's collection.

    Args:
        books (list): A list of Book objects representing the library's collection.
    """
    if not books:
        print("No books found.")
    else:
        for book in books:
            print("---------------------------")
            print(book)
            print("---------------------------")

def search_books(books, search_term):
    """Searches for books in the library's collection based on a search term.

    Args:
        books (list): A list of Book objects representing the library's collection.
        search_term (str): The term to search for (can be title, author, or ISBN).

    Returns:
        list: A list of Book objects matching the search criteria.
    """
    search_results = [book for book in books if search_term.lower() in book.title.lower() or
                      search_term.lower() in book.author.lower() or
                      search_term.lower() in book.isbn.lower()]
    return search_results
