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