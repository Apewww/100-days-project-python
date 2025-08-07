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