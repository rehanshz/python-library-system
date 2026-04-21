from utils import issue_books, books
from datetime import datetime

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def return_book():
    book_name = input("Enter book name: ").upper()

    if book_name in issue_books:

        issued_date = datetime.strptime(
            issue_books[book_name]["date"], "%d-%m-%Y"
        )
        due_days = issue_books[book_name]["due"]
        user_date = input("Enter return date (DD-MM-YYYY): ")

        today = datetime.strptime(user_date, "%d-%m-%Y")
        total_days = (today - issued_date).days

        late_days = total_days - due_days

        if late_days > 0:
            week = (late_days // 7) + 1

            fine_per_day = 10 * factorial(week)
            total_fine = fine_per_day * late_days

            print(f"Late by {late_days} days")
            print(f"Fine per day: ₹{fine_per_day}")
            print(f"Total fine: ₹{total_fine}")
        else:
            print("Returned on time. No fine.")

        # return book
        issue_books.pop(book_name)
        books[book_name] = "Available"

        print(f"{book_name} returned successfully")

    else:
        print("Only issued books can be returned")