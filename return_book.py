from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        issue_books.pop(book_name)
        books[book_name]="Available"
        print(f" {book_name} returned, Successfully")
    else:
        print("Only issued books can be returned")