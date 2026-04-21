from utils import books, issue_books,user_details
from datetime import datetime

def issue():
    book_name = input("Enter book name: ").upper()
    
    if book_name in books:
        books.pop(book_name)
        user=input("Please enter your good name:")
        timeperiod=int(input("Number of days book is issued for"))
        issue_books[book_name]={
            "status": "ISSUED",
            "date": datetime.now().strftime("%d-%m-%Y"),
            "user_name":user,
            "due":timeperiod}
        
    else:
        print("Sorry This book is not available")
    print("""
====Notice====
If issuer failes to return book within the alloted time period
charges will be applied like
for 1 week : 10Rs/day/book
2nd week : 10*2/day/book
3rd week : 10*2*3/day/book
 And so on ....""")