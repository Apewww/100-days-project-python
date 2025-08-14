# What is a Canvas Widget?
# canvas = tk.Canvas(root, width=100, height=300, bg="white")
# canvas.pack()

# Drawing Shapes and Lines
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Example")
# root.geometry("400x400")

# canvas = tk.Canvas(root, width=400, height=400, bg="white")
# canvas.pack()

# canvas.create_line(10, 10, 200, 200, fill="blue", width=3)
# canvas.create_rectangle(50, 50, 150, 150, outline="red", width=2)
# canvas.create_oval(200, 50, 350, 200, outline="green", width=2)

# root.mainloop()

# Handling Mouse Events on Canvas
# import tkinter as tk

# root = tk.Tk()
# root.title("Mouse Drawing")
# root.geometry("400x400")

# canvas = tk.Canvas(root, width=400, height=400, bg="white")
# canvas.pack()

# def draw(event):
#     x, y = event.x, event.y
#     canvas.create_oval(x, y, x+2, y+2, fill="black", outline="black")
    
# canvas.bind("<B1-Motion>", draw)

# root.mainloop()

# Clearing and Resetting the Canvas
# import tkinter as tk

# root = tk.Tk()
# root.title("Clear Canvas")
# root.geometry("400x400")

# canvas =  tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# def draw(event):
#     x,y = event.x, event.y
#     canvas.create_oval(x, y, x+2,  y+2, fill="black", outline="black")
    
# def clear_canvas():
#     canvas.delete("all")
    
# canvas.bind("<B1-Motion>", draw)

# clear_btn = tk.Button(root, text="Clear Canvas", command=clear_canvas)
# clear_btn.pack(pady=20)

# root.mainloop()


# Day 32 Project: Drawing Pad App
import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Drawing Pad App")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

current_color = "black"
current_size = 2

canvas = tk.Canvas(root, width=500, height=450, bg="white", relief="ridge", bd=2)
canvas.pack(pady=20)

def draw(event):
    x,y = event.x, event.y
    canvas.create_oval(
        x - current_size, y - current_size,
        x + current_size,  y + current_size,
        fill=current_color, outline=current_color
    )
    
def clear_canvas():
    canvas.delete("all")

def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def change_size(value):
    global current_size
    current_size = int(value)
    
canvas.bind("<B1-Motion>", draw)

control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack()

color_btn = tk.Button(control_frame, text="Choose Color", command=change_color, bg="#9CD3B8", font=("Arial", 14))
color_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(control_frame, text="Clear Canvas", command=clear_canvas, bg="#9CD3B8", font=("Arial", 14))
clear_btn.grid(row=0, column=1, padx=10)

size_label = tk.Label(control_frame, text="Size", bg="#f0f0f0", font=("Arial", 14))
size_label.grid(row=0, column=2, padx=10)

size_slider = tk.Scale(control_frame, from_=1, to=10, orient="horizontal", command=change_size, font=("Arial", 14))
size_slider.set(2)
size_slider.grid(row=0, column=3, padx=10)

root.mainloop()