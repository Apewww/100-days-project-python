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

root = tk.Tk()
root.title("Button State Management")
root.geometry("300x200")

def toggle_button():
    if button['state'] == 'normal':
        button.config(state='disabled')
        toggle_btn.config(text='Enable Button')
    else:
        button.config(state='normal')
        toggle_btn.config(text="I am Activate")
        
# Buttons
button = tk.Button(root, text="I am Active")
button.pack(pady=10)

toggle_btn = tk.Button(root, text="Disable Button", command=toggle_button)
toggle_btn.pack(pady=10)

root.mainloop()