# The Mini ATM Machine will Allow users to:

# Authenticate with PINs securely
# Check account balance.
# Deposit Money
# Withdraw money with balance validation.
# Change PIN 
# Exit securely

# Classes Overview:

# BankAccount:
# Attributes: account_number, pin_balance
# Methods: check_balance(), deposit(), withdraw(), change_pin()

# ATM
# Manages account authentication
# Provides the main menu for users.

# Concepts Applied:
# Encapsulation: Secure PIN Handling and balance access
# Static Method: For utility tasks like PIN Validation
# Class Method: To maintain account-level settings.
# Polymorphism: Flexibility in transactions operations.

# Mini ATM Machine

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        
    # Validate Pin
    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    # Check Balance
    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
        
    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid Deposit Amount")
            
    # Withdraw Money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid Withdrawal Amount")
            
    # Change Pin
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("Pin Changed Successfully")
        else:
            print("Failed to Change PIN, Ensure the old pin is correct and the new PIN is 4 digits")

class ATM:
    def __init__(self):
        self.account = {}
        
    # Validate Data
    def validate_account(self, account_number):
        for akun in self.account:
            if account_number == akun:
                return True
        return False
        
    # Create Account
    def create_account(self):
        account_number = input("Enter account number: ")
        pin = input("Set a 4-digit PIN: ")
        if self.validate_account(account_number):
            print("Account Number already exists")
            return False
        if len(pin) == 4 and pin.isdigit():
            self.account[account_number] = BankAccount(account_number, pin)
            print("Account Created Successfully")
        else:
            print("Invalid PIN, Ensure it's 4 digits")
            
    # Authentication Account
    def authenticate_account(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        
        account = self.account.get(account_number)
        if account and account.validate_pin(pin):
            print("Account Authenticated Successfully")
            self.account_menu(account)
        else:
            print("Invalid Account Number or PIN")
            return None
        
    # Account Menu
    def account_menu(self, account):
        while True:
            print("\n----- ATM Menu -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")
            
            choice = input("Enter your choice(1-5): ")
            
            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new 4-digit PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
                
    # Main Menu
    def main_menu(self):
        while True:
            print("\n----- Welcome to Mini ATM Machine -----")
            print("1. Create Account")
            print("2. Login to Account")
            print("3. Exit")
            
            choice = input("Choose an option(1-3): ")
            
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.authenticate_account()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
            
# Start the ATM Machine
if __name__ == '__main__':
    atm = ATM()
    atm.main_menu()