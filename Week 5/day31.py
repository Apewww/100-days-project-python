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
# import tkinter as tk

# root = tk.Tk()
# root.title("Displaying Dynamic Results")
# root.geometry("300x200")

# entry = tk.Entry(root)
# entry.pack(pady=10)

# result_label = tk.Label(root, text="Result will be displayed here.")
# result_label.pack(pady=10)

# def update_label():
#     text = entry.get()
#     result_label.config(text=f"You entered: {text}")
    
# button = tk.Button(root, text="Update Label", command=update_label)
# button.pack(pady=10)

# root.mainloop()

# Using Entry Widget with Labels and Buttons
# Day 31 Project: BMI Calculator

import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#f0f4c3")

# Title Label
tittle_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20), bg="#f0f4c3")
tittle_label.pack(pady=20)

# Weight Input
weight_label = tk.Label(root, text="Enter your weight (kg):", font=("Arial", 14), bg="#f0f4c3")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 14), width=20)
weight_entry.pack(pady=5)

# Height Input
height_label = tk.Label(root, text="Enter your height (m):", font=("Arial", 14), bg="#f0f4c3")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 14), width=20)
height_entry.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4c3")
result_label.pack(pady=20)

# Calculate BMI Function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        bmi = weight / (height ** 2)
        status = ""
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obese"
        result_label.config(text=f"BMI: {bmi:.2f}\n Status: {status}", fg="green")
    except ValueError:
        result_label.config(text="Invalid input. Please enter positive numbers.", fg="red")

# Buttons
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Arial", 14), bg="#f0f4c3")
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="")], font=("Arial", 14), bg="#f0f4c3")
reset_button.pack(pady=5)

# Run the app
root.mainloop()