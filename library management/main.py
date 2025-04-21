from books import books
from students import students

class Library:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id

    def studentVerification(self):
        if self.student_id in students:
            print(f"Hey, {self.student_name}, you are allowed to borrow books from this library.")
            return True
        else:
            print(f"Sorry! {self.student_name}, you are not registered in this library.")
            return False

    def bookBorrow(self, book_name):
        normalized_book_name = book_name.strip().title()
        
        if normalized_book_name in books:
            if books[normalized_book_name]["status"] == "available":
                print(f"The book: {book_name} is successfully borrowed.")
                books[normalized_book_name]["status"] = "unavailable"
            else:
                print(f"The book: {book_name} is currently unavailable in the library.")
        else:
            print(f"The book: {book_name} is not available in this library.")

    def bookReturn(self, book_name):
        normalized_book_name = book_name.strip().title()
        
        if normalized_book_name in books:
            if books[normalized_book_name]["status"] == "unavailable":
                print(f"The book: {book_name} has been successfully returned.")
                books[normalized_book_name]["status"] = "available"
            else:
                print(f"The book: {book_name} is already available in the library.")
        else:
            print(f"The book: {book_name} is not available in this library.")

user_action = int(input('''
What would you like to do?
1. Borrow a book
2. Return a book
Choose an option: '''))

student_id = int(input("Enter your student ID: "))
student_name = input("Enter your name: ").strip()

library = Library(student_name, student_id)

if library.studentVerification():
    book_name = input("Enter the name of the book: ").strip()

    if user_action == 1:
        library.bookBorrow(book_name)
    elif user_action == 2:
        library.bookReturn(book_name)
    else:
        print("Invalid option.")

print("\nCurrent status of books in the library:")
for book_name, details in books.items():
    print(f"{book_name}: {details['status']}")
