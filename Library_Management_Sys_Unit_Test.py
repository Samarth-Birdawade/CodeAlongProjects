import unittest
from unittest.mock import patch
import io
from Library_Management_Sys import *

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh library and books for every test case."""
        self.lib = library("CA Library", 5)
        self.book1 = books("Lord of the Flies", "William Golding", 999)
        self.book2 = books("Hamlet", "Shakespeare", 499)

    def test_add_book_increases_count(self):
        """Verify that adding a book updates the list and the count."""
        initial_count = self.lib.no_of_books
        self.lib.add_book(self.book1)
        self.assertIn(self.book1, self.lib.books_list)
        self.assertEqual(self.lib.no_of_books, initial_count + 1)

    def test_borrow_book_success(self):
        """Verify that borrowing a book changes its availability."""
        self.lib.add_book(self.book1)
        self.lib.borrow_book("Lord of the Flies")
        self.assertFalse(self.book1.is_available)

    def test_borrow_unavailable_book_error(self):
        """Verify that a Book_Error is raised if the book isn't in the library."""
        with self.assertRaises(Book_Error):
            self.lib.borrow_book("Non-existent Book")

    def test_return_book_success(self):
        """Verify that returning a book makes it available again."""
        self.lib.add_book(self.book1)
        self.book1.is_available = False
        self.lib.return_book("Lord of the Flies")
        self.assertTrue(self.book1.is_available)

    def test_return_unborrowed_book_error(self):
        """Verify that returning a book that was never borrowed raises Book_Error."""
        self.lib.add_book(self.book1)
        with self.assertRaises(Book_Error):
            self.lib.return_book("Lord of the Flies")

    @patch('sys.stdout', new_callable = io.StringIO)
    def test_book_deletion_output(self, mock_stdout):
        """Test the __del__ destructor message using mocking."""
        temp_book = books("To Kill a Mockingbird", "Harper Lee", 699)
        book_name = temp_book.book_name
        del temp_book
        self.assertIn(f"The book '{book_name}' has been removed", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()