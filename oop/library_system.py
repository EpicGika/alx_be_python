# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize the book with title and author."""
        self.title = title
        self.author = author

    def get_details(self):
        """Return basic details of the book."""
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        """String representation for the Book class."""
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # Additional attribute for EBook

    def get_details(self):
        """Return details specific to an EBook, including file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __str__(self):
        """String representation for the EBook class."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Additional attribute for PrintBook

    def get_details(self):
        """Return details specific to a PrintBook, including page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count} pages"

    def __str__(self):
        """String representation for the PrintBook class."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count} pages"


# Composition - Library Class
class Library:
    def __init__(self):
        """Initialize the Library with an empty collection of books."""
        self.books = []  # A list to store instances of books

    def add_book(self, book):
        """Add a book to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library with their details."""
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)  # Use the __str__ method for each book
