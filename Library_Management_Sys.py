import logging

# Custom Exception for handling book related errors
class Book_Error(Exception):
    def __init__(self, error_message="Book related error occurred"):
        super().__init__(error_message)

class library:
    def __init__(self, name, no_of_books):
        self.name = name
        self.no_of_books = no_of_books
        self.books_list = []

    def add_book(self, book):
        if self.no_of_books <= 0:
            logging.error("Cannot add more books, library is full.")
        if book in self.books_list:
            logging.warning(f"The book '{book.book_name}' is already in the library.")
            return
        self.books_list.append(book)
        self.no_of_books += 1
        print(f"Book '{book.book_name}' added to the library.")
    
    def borrow_book(self, book_name):
        for book in self.books_list:
            if book.book_name == book_name:
                book.borrow_book()
                return
        raise Book_Error(f"Book '{book_name}' is not available in the library.")
    
    def return_book(self, book_name):
        for book in self.books_list:
            if book.book_name == book_name:
                book.return_book()
                return
        raise Book_Error(f"Book '{book_name}' does not belong to this library.")

class books:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price
        self.is_available = True

    def __del__(self):
        print(f"The book '{self.book_name}' has been removed from the library.")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed the book '{self.book_name}' by {self.author}.")
        else:
            print(f"The book '{self.book_name}' is currently not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned the book '{self.book_name}' by {self.author}.")
        else:
            raise Book_Error(f"The book '{self.book_name}' was not borrowed.\nPlease check book details again.")


if __name__ == "__main__":
    lib = library("My Library", 3)

    book1 = books("Hamlet", "Shakespeare", 499)
    lib.add_book(book1)
    lib.borrow_book("Hamlet")

    book2 = books("To Kill a Mockingbird", "Harper Lee", 999)
    lib.add_book(book2)
    lib.borrow_book("To Kill a Mockingbird")
    lib.return_book("To Kill a Mockingbird")

    book3 = books("How to get away with Muder", "Agatha Christie", 799)
    lib.add_book(book3)
    lib.return_book("How to get away with Muder")