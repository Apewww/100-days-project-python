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

