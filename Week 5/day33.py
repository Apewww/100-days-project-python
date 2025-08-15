# What are Message Boxes?
# from tkinter import messagebox
# messagebox.showinfo("Title", "This is an information message.")

# Types of Message Boxes
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.withdraw()

# messagebox.showinfo("Info", "This is an info message.")
# messagebox.showinfo("Warning", "This is an info message.")
# messagebox.showinfo("Error", "This is an info message.")

# response = messagebox.askyesno("Question", "Do you want to continue?")
# print(response)

# Using Message Boxes for Validation
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Validation Example")
# root.geometry("300x200")

# entry = tk.Entry(root)
# entry.pack(pady=10)

# def validate_input():
#     user_input = entry.get()
#     if user_input.strip() == "":
#         messagebox.showerror("Error", "Please enter a value.")
#     else:
#         messagebox.showinfo("Success", f"You entered: {user_input}")
        
# button = tk.Button(root, text="Submit", command=validate_input)
# button.pack(pady=10)

# root.mainloop()

# Handling User Authentication
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Simple Login")
# root.geometry("300x200")

# users = "admin"
# passw = "123"

# tk.Label(root, text="Username:").pack()
# username_entry = tk.Entry(root)
# username_entry.pack()

# tk.Label(root, text="Password:").pack()
# password_entry = tk.Entry(root, show="*")
# password_entry.pack()

# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#     if username == users and password == passw:
#         messagebox.showinfo("Success", "Login successful!")
#     else:
#         messagebox.showerror("Error", "Invalid username or password.")
        
# login_btn = tk.Button(root, text="Login", command=login)
# login_btn.pack()

# root.mainloop()

# Day 33 Project: Simple Login System
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Login System")
root.geometry("400x300")
root.configure(bg="#f0f4c3")

USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "user123"
}

title_label = tk.Label(root, text="Login System", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

username_label = tk.Label(root, text="Username", font=("Arial", 14), bg="#f0f4c3")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 14), width=30)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password", font=("Arial", 14), bg="#f0f4c3")
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 14), width=30, show="*")
password_entry.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        
def clear():
    username_entry.delete(0,  tk.END)
    password_entry.delete(0,  tk.END)
    
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 14), bg="#4CAF50", fg="#fff")
login_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 14), bg="#4CAF50", fg="#fff")
clear_button.pack(pady=10)

button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14), bg="#4CAF50", fg="#fff")
button.pack(pady=5)

root.mainloop()