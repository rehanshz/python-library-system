from utils import books

def add():
    book_name = input("Enter the title of the book to add: ").upper()
    books[book_name]="Available"
    print(f"'{book_name}' is now available in the library.")
    