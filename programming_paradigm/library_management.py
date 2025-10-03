class Book:
    """A class representing a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"Book '{title}' is not available.")
        return False

    def return_book(self, title):
        """Return a book by its title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"Book '{title}' was not checked out.")
        return False

    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
