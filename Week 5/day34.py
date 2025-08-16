# Introduction to Adavanced Tkinter Widgets
# Using Listbox for Dynamic Lists
# import tkinter as tk

# root = tk.Tk()
# root.title("Listbox Example")
# root.geometry("300x200")

# listbox = tk.Listbox(root)
# listbox.pack(pady=10)

# listbox.insert(tk.END, "Task 1")
# listbox.insert(tk.END, "Task 2")

# def get_selected():
#     selected = listbox.get(tk.ACTIVE)
#     print("Selected:", selected)
    
# button = tk.Button(root, text="Get Selected", command=get_selected)
# button.pack(pady=10)

# root.mainloop()

# Scrollbar Intergration
# import tkinter as tk

# root = tk.Tk()
# root.title("Listbox with ScrollBar")
# root.geometry("300x200")

# frame = tk.Frame(root)
# frame.pack(pady=10)

# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# listbox =  tk.Listbox(frame, yscrollcommand=scrollbar.set, height=10)
# listbox.pack()

# scrollbar.config(command=listbox.yview)

# for i in range(1, 21):
#     listbox.insert(tk.END, f"Item {i}")
    
# root.mainloop()
    
# Handling User Actions (Add, Delete, Clear)
# import tkinter as tk

# root = tk.Tk()
# root.title("Listbox Management")
# root.geometry("300x200")

# listbox = tk.Listbox(root)
# listbox.pack(pady=10)

# def add_item():
#     item = entry.get()
#     if item:
#         listbox.insert(tk.END, item)
#         entry.delete(0, tk.END)
        
# def delete_item():
#     selected = listbox.curselection()
#     if selected:
#         listbox.delete(selected[0])
        
# entry = tk.Entry(root)
# entry.pack(pady=5)

# add_button = tk.Button(root, text="Add Item", command=add_item)
# add_button.pack(pady=5)

# delete_button = tk.Button(root, text="Delete Item", command=delete_item)
# delete_button.pack(pady=5)

# root.mainloop()

# Day 34 Project: To-Do List Gui
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="#e3f2fd")

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task")
        
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showerror("Error", "Please select a task")
        
def clear_task():
    task_listbox.delete(0, tk.END)
    
title_label = tk.Label(root, text="To-Do App List", font=("Arial", 20), bg="#e3f2fd")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=40, font=("Arial", 14), bg="#d2f2f5")
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 14), bg="#4CAF50")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 14), bg="#A72F2F")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Button", command=clear_task, font=("Arial", 14), bg="#A72F2F")
clear_button.grid(row=0, column=2, padx=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 14), bg="#d2f2f5")
task_listbox.pack(pady=10)

scrollbar.config(command=task_listbox.yview)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14), bg="#A72F2F")
exit_button.pack(pady=10)

root.mainloop()