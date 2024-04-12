import sys
import unittest
from unittest.mock import patch
from io import StringIO
from main import *
from book import Book, create_book, update_book, delete_book_by_isbn, list_books, search_books
from user import User, create_user, update_user, delete_user_by_id, list_users
from check import check_availability, borrow_book, return_book
from store import save_data, load_data

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        # Create some sample data for testing
        self.books = [
            Book("Title1", "Author1", "ISBN1"),
            Book("Title2", "Author2", "ISBN2"),
            Book("Title3", "Author3", "ISBN3")
        ]
        self.users = [
            User("User1", "ID1"),
            User("User2", "ID2"),
            User("User3", "ID3")
        ]

    def test_check_availability(self):
        # Test check_availability function
        self.assertTrue(check_availability(self.books, "ISBN1"))
        self.assertFalse(check_availability(self.books, "ISBN4"))

    @patch('builtins.input', side_effect=["Title4", "Author4", "ISBN4"])
    def test_create_book(self, mock_input):
        # Test create_book function
        new_book = create_book()
        self.assertEqual(new_book.title, "Title4")
        self.assertEqual(new_book.author, "Author4")
        self.assertEqual(new_book.isbn, "ISBN4")

    def test_update_book(self):
        # Test update_book function
        update_book(self.books, "ISBN1")
        updated_book = [book for book in self.books if book.isbn == "ISBN1"]
        self.assertIsNotNone(updated_book)
        self.assertEqual(updated_book[0].title, "New Title")

    def test_list_books(self):
        # Test list_books function
        captured_output = StringIO()
        sys.stdout = captured_output
        list_books(self.books)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertIn("Title1", captured_output.getvalue())

    def test_search_books(self):
        # Test search_books function
        search_results = search_books(self.books, "Author2")
        self.assertIsNotNone(search_results)
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].author, "Author2")

    def test_create_user(self):
        # Test create_user function
        new_user = create_user(self.users)
        self.assertEqual(new_user.name, "New User")
        self.assertEqual(new_user.user_id, "New ID")

if __name__ == "__main__":
    unittest.main()
