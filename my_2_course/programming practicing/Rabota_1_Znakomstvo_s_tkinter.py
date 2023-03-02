from tkinter import *
import math

root = Tk()

# Variables
oval_radius = 200
size = oval_radius * 3
point_radius = oval_radius - 50
speed = 10
precision = 0.01
point_size = 50

# creating window and surface
canvas = Canvas(root, width=size, height=size)
canvas.pack()

# creating circle
oval = canvas.create_oval(size / 2 - oval_radius, size / 2 - oval_radius, size / 2 + oval_radius,
                          size / 2 + oval_radius, outline="green")


def move_point(start_point, direction):
    global px, py
    if direction == "r":
        x = oval_radius + point_radius * math.cos(start_point)
        y = oval_radius + point_radius * math.sin(start_point)
        canvas.move(point, x - px, y - py)
        px, py = x, y
        root.after(speed, move_point, start_point + precision, direction)
    elif direction == "l":
        x = oval_radius + point_radius * math.sin(start_point)
        y = oval_radius + point_radius * math.cos(start_point)
        canvas.move(point, x - px, y - py)
        px, py = x, y
        root.after(speed, move_point, start_point + precision, direction)
    else:
        raise Exception(f"Not valid direction \"{direction}\". Should be \"right\" or \"left\"")


px = -((point_radius + 50) / 2 - point_size / 2)
py = -((point_radius + 50) / 2 - point_size / 2)

# creating point
point = canvas.create_oval(0, 0, point_size, point_size, fill='green')

move_point(start_point=math.pi, direction="r")

root.mainloop()
