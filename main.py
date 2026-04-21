from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book

def library():
    while True:
        print("""----📚LIBRARY MANAGEMENT SYSTEM-------
HOW CAN WE HELP YOU!!!!
1. ADD BOOKS 
2. SHOW AVAILABLE BOOKS 
3. ISSUE BOOKS
4. RETURN BOOKS 
5. EXIT!!!!""")
        choice = int(input("Enter your choice: "))
        
        if choice==1:   add()
        elif choice==2: show()
        elif choice==3: issue()
        elif choice==4: return_book()
        elif choice==5: 
            print("Thanks for using the library system\nsee you again😉")
            break
        else:
            print("Sorry, Invalid choice")
            
library()