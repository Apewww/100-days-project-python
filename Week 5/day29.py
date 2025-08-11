# Introduction
import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.title("My First GUI App")
# root.geometry("300x200")

# # Start the GUI event loop
# root.mainloop()

# Main Window
# root = tk.Tk()
# root.title("Simple GUI Example")
# root.geometry("300x200")

# # Add Label
# label = tk.Label(root, text="Hello, World!", font=("Arial", 14))
# label.pack(pady=10)

# # Add Entry
# entry = tk.Entry(root, width=20)
# entry.pack(pady=10)

# # Add Button
# def on_click():
#     text = entry.get()
#     label.config(text=f"Hello, {text}!")
    
# button = tk.Button(root, text="Click Me!", command=on_click)
# button.pack(pady=10)

# # Run the application
# root.mainloop()

# root = tk.Tk()
# root.title("Event Handling Example")
# root.geometry("300x200")

# # Add Widgets
# label = tk.Label(root, text="Enter your name: ")
# label.pack()

# entry = tk.Entry(root)
# entry.pack()

# def greet():
#     name = entry.get()
#     label.config(text=f"Hello, {name}!")
    
# button = tk.Button(root, text="Greet", command=greet)
# button.pack()

# root.mainloop()


# Day 29 Project: Simple GUI App

root = tk.Tk()

# Main Window
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="#F0f0f0")

# Title Label
titel_label = tk.Label(root, text="Welcome to My GUI App!", font=("Arial", 18), bg="#f0f0f0")
titel_label.pack(pady=20)

# Name Entry
name_label = tk.Label(root, text="Enter your name: ", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Greeting Function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", fg="green")
    else:
        greeting_label.config(text="Please enter your name!", fg="red")
        
# Reset Function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")
    
# Greet Button
greet_button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 12), bg="#4CAF50", fg="white")
greet_button.pack(pady=10)

# Reset Button
greet_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="#4CAF50", fg="white")
greet_button.pack(pady=5)

# Greeting Label
greeting_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
greeting_label.pack(pady=20)

# Run the Application
root.mainloop()