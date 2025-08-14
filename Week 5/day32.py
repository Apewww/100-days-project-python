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
import tkinter as tk

root = tk.Tk()
root.title("Clear Canvas")
root.geometry("400x400")

canvas =  tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

def draw(event):
    x,y = event.x, event.y
    canvas.create_oval(x, y, x+2,  y+2, fill="black", outline="black")
    
def clear_canvas():
    canvas.delete("all")
    
canvas.bind("<B1-Motion>", draw)

clear_btn = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_btn.pack(pady=20)

root.mainloop()


# Day 32 Project: Drawing Pad App