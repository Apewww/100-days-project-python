# Introduction

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password # Private Attributes
    
#     def get_password(self):
#         return "*****"
    
#     def set_password(self, new_password):
#         if len(new_password) > 0:
#             self.__password = new_password
#             print("Password updated successfully")
#         else:
#             print("Password must be at least 8 characters")
            
# user = User("Rafly", "rafly123")
# print(user.username)
# print(user.get_password())
# user.set_password("test123")

# class UserProfile:
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.__password = password
        
#     def show_profile(self):
#         print(f"Username: {self.username}")
#         print(f"Email: {self._email}")
#         print(f"Password: {self.__password}")
        
# user = UserProfile("Rafly", "rafly@gmail.com", "12345")
# print(user.username)
# # print(user._email)
# # print(user.__password)
# # print(user._UserProfile__password)
# user.show_profile()

# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, new_balance):
#         if new_balance >= 0:
#             self.__balance = new_balance
#             print("Balance updated successfuly")
#         else:
#             print("Balance must be at least 0")
            
# account = Account(1000)
# print(account.get_balance())
# account.set_balance(5000)
# print(account.get_balance())

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.__password = None
        
#     def set_password(self, new_password):
#         if len(new_password) < 6:
#             print("Password must be at least 6 characters")
#         else:
#             self.__password = new_password
#             print("Password set successfully")
            
#     def get_password(self):
#         return self.__password
    
# user = User("Rafly")
# user.set_password("123456")
# print(user.get_password())

# Secure User Profile App
class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = None
        self.set_password(password)
        
    # Getter for email
    def get_email(self):
        return self._email
    
    # Seteter for Email
    def set_mail(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("Email updated sucessfully")
        else:
            print("Invalid email format")
            
    # Setter for password
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Password must be at least 6 characters")
            return False
        else:
            self.__password = new_password
            print("Password updated successfully")
            return True
            
    # Display Profile
    def display_profile(self):
        print("\n----- User Profile -----")
        print(f"Username: {self.username}")
        print(f"Email: {self.get_email()}")
        print(f"Password: {self.__password}")
        
# Main Program
users = []

def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = UserProfile(username, email, password)
    if user._UserProfile__password is not None:
        users.append(user)
        print("User created successfully")

def view_profile():
    if not users:
        print("No users found")
    else:
        for user in users:
            user.display_profile()
            
def update_email():
    username = input("Enter username to update email: ")
    for user in users:
        if user.username == username:
            new_email = input("Enter new email: ")
            user.set_mail(new_email)
            return
    print("User not found")
    
# Main Menu
while True:
    print("\n----- Secure User Profile App -----")
    print("1. Create User")
    print("2. View Profile")
    print("3. Update Email")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        create_user()
    elif choice == '2':
        view_profile()
    elif choice == '3':
        update_email()
    elif choice == '4':
        print("Exiting Program.")
        break
    else:
        print("Invalid Choice, please choice (1-4)")