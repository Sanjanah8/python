import tkinter as tk

def draw():
    canvas.create_line(0, 0, 200, 200, fill="blue")
    canvas.create_rectangle(50, 50, 150, 150, fill="red")

root = tk.Tk()
root.title("Drawing with Tkinter")
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

draw()
root.mainloop()
