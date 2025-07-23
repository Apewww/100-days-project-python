# Introduction
# import math
# print(math.sqrt(16))

# import random
# print(random.randint(1,10))

# from random import choices
# print(choices(['Apple','Banana','Orange']))

# import random as r
# print(r.randint(1,10))

# from random import *
# print(randint(1,10))

# import random

# password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=12))
# print(password)

# import greetings

# print(greetings.say_hello('Apew'))

# import random
# attemp = 0
# dummy_password = 'apew'
# find = False
# while find != True:
#     attemp += 1
#     password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4))
#     if password == dummy_password:
#         print("Password is:",password) 
#         print("Total attemps:", attemp)
#         break


import random, string

# Step 1: Define Password Generation Function
def generate_password(lenght=12):
    if lenght < 4:
        raise ValueError("Password lenght must be at least 4 characters")

    # Characters sets for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=?><,.|}{[]}"
    
    # Ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the remaining lenght with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=lenght - 4)
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

# Step 2: User Interaction
try:
    password_length = int(input("Enter the password length (minimum 4): "))
    password = generate_password(password_length)
    print("Password Generated:", password)
except ValueError as e:
    print(e)