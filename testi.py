import unittest
from unittest.mock import patch
from main import *
from book import *
from user import *
from check import *

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
        new_book = create_book(self.books)
        self.assertEqual(new_book.title, "Title4")
        self.assertEqual(new_book.author, "Author4")
        self.assertEqual(new_book.isbn, "ISBN4")

    def test_delete_book_by_isbn(self):
        # Test delete_book_by_isbn function
        delete_book_by_isbn(self.books, "ISBN1")
        self.assertEqual(len(self.books), 2)
        self.assertNotIn("ISBN1", [book.isbn for book in self.books])

    def test_delete_user_by_id(self):
        # Test delete_user_by_id function
        delete_user_by_id(self.users, "ID1")
        self.assertEqual(len(self.users), 2)
        self.assertNotIn("ID1", [user.user_id for user in self.users])

if __name__ == "__main__":
    unittest.main()
