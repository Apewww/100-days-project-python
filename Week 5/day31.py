# Understanding Inpit Fields in Tkinter
# import tkinter as tk

# root = tk.Tk()
# root.title("Input Field Example")
# root.geometry("300x200")

# entry = tk.Entry(root, width=25)
# entry.pack(pady=10)

# def display_input():
#     user_input = entry.get()
#     print("User Input:", user_input)

# button = tk.Button(root, text="Submit", command=display_input)
# button.pack(pady=10)

# root.mainloop()

# Getting and Validating User Input
# import tkinter as tk

# root = tk.Tk()
# root.title("Input Validation")
# root.geometry("300x200")

# entry = tk.Entry(root)
# entry.pack(pady=10)

# def validate_input():
#     try:
#         value = float(entry.get())
#         print(f"Valid Input: {value}")
#     except ValueError:
#         print("Invalid Input: Please enter a number")
        
# button = tk.Button(root, text="Validate", command=validate_input)
# button.pack(pady=10)

# root.mainloop()

# Displaying Dynamic Results
import tkinter as tk

root = tk.Tk()
root.title("Displaying Dynamic Results")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady=10)

result_label = tk.Label(root, text="Result will be displayed here.")
result_label.pack(pady=10)

def update_label():
    text = entry.get()
    result_label.config(text=f"You entered: {text}")
    
button = tk.Button(root, text="Update Label", command=update_label)
button.pack(pady=10)

root.mainloop()Using Entry Widget with Labels and Buttonssssssssszzz

# Day 31 Project: BMI Calculator