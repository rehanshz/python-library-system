from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books:
        books.pop(book_name)
        issue_books[book_name]="issued"
        print("Book assigned successfully")
    else:
        print("Sorry This book is not available")