# import tkinter as tk

# root = tk.Tk()
# root.title("Click Counter App")

# label = tk.Label(root, text="Hellow", bg="red")
# label.pack()

# # entry = tk.Entry(root)
# # entry.pack()

# count = 0
# def counter():
#     global count
#     count += 1
#     label.config(text=f"{count}") 

# button = tk.Button(root, text="Counter", command=counter)
# button.pack()

# root.mainloop()

# Introduction

import tkinter as tk

# # Main Window
# root = tk.Tk()
# root.title("Basic Button Example")
# root.geometry("300x200")

# # Button Click Handler
# def on_click():
#     print("Button Clicked!")
    
# # Create Button
# button = tk.Button(root, text="Click Me", command=on_click)
# button.pack(pady=20)

# # Run the application
# root.mainloop()

# root = tk.Tk()
# root.title("Button Events")
# root.geometry("300x200")

# # Event Handlers
# def on_enter(event):
#     button.config(text="Mouse Over")
    
# def on_leave(event):
#     button.config(text="Mouse Out")
    
# # Create Button
# button = tk.Button(root, text="Hover Me")
# button.pack(pady=20)

# # Bind Events
# button.bind("<Enter>", on_enter)
# button.bind("<Leave>", on_leave)

# root.mainloop()

# root = tk.Tk()
# root.title("Dynamic Button Counter")
# root.geometry("300x200")

# # Counter Variable
# counter = 0

# def increment_counter():
#     global counter
#     counter += 1
#     label.config(text=f"Count: {counter}")
    
# # Label and Button
# label = tk.Label(root, text="Count: 0", font=("Arial", 14))
# label.pack(pady=10)

# button = tk.Button(root, text="Click Me", command=increment_counter)
# button.pack(pady=10)

# root.mainloop()

# root = tk.Tk()
# root.title("Button State Management")
# root.geometry("300x200")

# def toggle_button():
#     if button['state'] == 'normal':
#         button.config(state='disabled')
#         toggle_btn.config(text='Enable Button')
#     else:
#         button.config(state='normal')
#         toggle_btn.config(text="I am Activate")
        
# # Buttons
# button = tk.Button(root, text="I am Active")
# button.pack(pady=10)

# toggle_btn = tk.Button(root, text="Disable Button", command=toggle_button)
# toggle_btn.pack(pady=10)

# root.mainloop()

# Day 30 Project: Click Counter App

# Main Window
root = tk.Tk()
root.title("Click Counter App")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

# Counter Variable
counter = 0

# Incement Function
def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")
    
# Reset Function
def reset():
    global counter
    counter = 0
    counter_label.config(text="Clicks: 0")
    
# Title Label
title_label = tk.Label(root, text="Click Counter", font=("Arial", 24), bg="#e3f2fd")
title_label.pack(pady=20)

# Counter Label
counter_label = tk.Label(root, text="Clicks: 0", font=("Arial", 16), bg="#e3f2fd")
counter_label.pack(pady=10)

# Increment Button
increment_button = tk.Button(root, text="Click Me", command=increment, font=("Arial", 12), bg="#e3f2fd")
increment_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 14), bg="#e3f2fd")
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14), bg="#e3f2fd")
exit_button.pack(pady=10)

# Run the App
root.mainloop()