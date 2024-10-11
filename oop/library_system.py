class Book:
    #Define a base class
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
            #Return basic details of the book.
        return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        
        self.file_size = file_size
    def get_details(self):
        return f"{super().get_details()}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_details(self):
        return f"{super().get_details()}, Page Count: {self.page_count} pages"

class Library:
    def __init__(self):
        """Initialize the Library with an empty collection of books."""
        self.books = []  # A list to store instances of books

    def add_book(self, book):
        #Add a book to the library's
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books available in the library.")

        else:
            for book in self.books:
                print(book.get_details())