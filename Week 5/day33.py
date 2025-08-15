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
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Login")
root.geometry("300x200")

USERNAME = "admin"
PASSWORD = "123"

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == USERNAME & password == PASSWORD:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        
login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

root.mainloop()


# Day 33 Project: Simple Login System