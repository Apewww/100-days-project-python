# Introduction

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
        
#     def display_info(self):
#         print(f"Tittle: {self.title}")
#         print(f"Author: {self.author}")
        
# # Create an object
# book1 = Book("2005", "Rafly Anggara Putra")
# book1.display_info()

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ${amount}. New Balance: ${self.balance}")
        
# account = BankAccount("Rafly Anggara Putra", 5000000)
# account.deposit(100000000)

# class Utiliy:
#     app_versionn = "1.0"
    
#     @classmethod
#     def get_version(cls):
#         print(f"App Version: {cls.app_versionn}")
        
#     def greet():
#         print("Hello!")
        
# Utiliy.get_version()
# Utiliy.greet()

# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
#         else: 
#             print("Invalid amount. Please enter a positive number.")
            
#     def get_balance(self):
#         return self.__balance
    
# account = Account("Rafly Anggara Putra", 5000000)
# account.deposit(50000)
# print(f"Account Balance: ${account.get_balance()}")

# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the Library")
        
    # View all books
    def view_books(self):
        if not self.books:
            print("No books in the Library")
        else:
            print("\n----- Library Catalog -----")
            for book in self.books:
                book.display_info()
                
    # Borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Book '{title}' has been borrowed. Enjoy Reading")
                return
        print(f"Book '{title}' is not available for borrowing.")
        
    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{title}' has been returned to the Library")
                return
        print(f"Book '{title}' is not in the library")
        
# Main Program
library = Library()

while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice = input("Enter your choice(1-5): ").strip()
    
    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        library.add_book(title,author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ").strip()
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ").strip()
        library.return_book(title)
    elif choice == "5":
        print("Exiting the Library Management System. Goodbye")
        break     
    else:
        print("Invalid choice. Please choose a valid option.")