# Introduction

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def display_info(self):
#         print(f"This is a {self.brand} {self.model}.")
        

# # Create an object
# my_car = Car("Tesla", "Model 3")
# my_car.display_info()

# your_car = Car("Honda", "Civic")
# your_car.display_info()

# class  Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.bread = breed
        
#     def bark(self):
#         print(f"{self.name} is barking!")
        
# # Create objects
# dog1 = Dog("Buddy", "Golden Retreiver")
# dog2 = Dog("Max", "Bulldog")

# dog1.bark()
# dog2.bark()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         print(f"Hello my name is {self.name} and I am {self.age} years old.")
        

# person1 = Person("John", 25)
# person1.greet()

# Bank Account Simulator
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        
    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0")
            
    # Withdraw Money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0 and not exceed current balance")
           
    # Show Accounts Details
    def show_details(self):
        print("\n----- Account Details -----")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")        
            
    # Check Balance
    # def check_balance(self):
    #     print(f"Account balance for {self.account_holder} is: ${self.balance}")
            
# Main Program
accounts = {}

def create_account():
    name = input("Enter account holder's name: ").strip()
    initial_deposit = float(input("Enter initial Deposit Amount: "))
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    print(f"Account created for {name} with initial deposit of ${initial_deposit}")
    
def access_account():
    name = input("Enter your name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n----- Account Menu -----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            
            choice = input("Enter your choice(1-4): ") 
            
            if choice == '1':
                amount = float(input("Enter deposit ammount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_details()
            elif choice == '4':
                print("Exiting account menu")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
    else:
        print("Account not found. Please create an account first.")
        
        
# Main Menu
while True:
    print("\n----- Bank Account Simulator -----")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("Enter your choice(1-3): ")
    
    if choice == '1':
        create_account()
    elif choice == '2':
        access_account()
    elif choice == '3':
        print("Exiting Bank Account Simulator")
        break
    else:
        print("Invalid choice. Please choose a valid option.")