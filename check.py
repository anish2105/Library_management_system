from book import Book
from store import save_data

def check_availability(books, isbn):
  """Checks if a book with the given ISBN is available for borrowing.

  Args:
      books: A list of Book objects representing the library's collection.
      isbn: The ISBN of the book to check.

  Returns:
      True if the book is available, False otherwise.
  """
  for book in books:
    if book.isbn == isbn and book.available:
      return True
  return False

def borrow_book(books, isbn, borrower_id, users):
  """Borrows a book with the given ISBN by a user with the specified ID.

  Args:
      books: A list of Book objects representing the library's collection.
      isbn: The ISBN of the book to borrow.
      borrower_id: The ID of the user borrowing the book.

  Returns:
      True if the book is borrowed successfully, False otherwise (e.g., not found or unavailable).
  """
  for i, book in enumerate(books):
    if book.isbn == isbn and book.available:
      book.available = False
      book.borrower_id = borrower_id
      print(f"Book with ISBN {isbn} borrowed successfully.")
      save_data(books, users)
      return True
  print(f"Book with ISBN {isbn} not found or unavailable.")
  return False

def return_book(books, isbn,users):
  """Returns a book with the given ISBN.

  Args:
      books: A list of Book objects representing the library's collection.
      isbn: The ISBN of the book to return.

  Returns:
      True if the book is returned successfully, False otherwise (e.g., not found).
  """
  for book in books:
    if book.isbn == isbn:
      book.available = True
      book.borrower_id = None
      print(f"Book with ISBN {isbn} returned successfully.")
      save_data(books, users)
      return True
  print(f"Book with ISBN {isbn} not found.")
  return False
