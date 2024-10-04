class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        self.title = title          # Public attribute for the title
        self.author = author        # Public attribute for the author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"You have checked out '{self.title}'.")

    def return_book(self):
        """Return the book to the library."""
        if not self._is_checked_out:
            print(f"'{self.title}' is not checked out.")
        else:
            self._is_checked_out = False
            print(f"You have returned '{self.title}'.")

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that holds books."""
    
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"'{title}' is not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' is not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No available books.")


# The following code is for testing and should be in main.py
if __name__ == "__main__":
    from library_management import Book, Library

    def main():
        # Setup a small library
        library = Library()
        library.add_book(Book("Brave New World", "Aldous Huxley"))
        library.add_book(Book("1984", "George Orwell"))

        # Initial list of available books
        print("Available books after setup:")
        library.list_available_books()

        # Simulate checking out a book
        library.check_out_book("1984")
        print("\nAvailable books after checking out '1984':")
        library.list_available_books()

        # Simulate returning a book
        library.return_book("1984")
        print("\nAvailable books after returning '1984':")
        library.list_available_books()

    main()
