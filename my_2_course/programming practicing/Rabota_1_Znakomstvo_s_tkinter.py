from tkinter import *
import math

root = Tk()

oval_radius = 200
size = oval_radius * 3
point_radius = oval_radius
speed = 10
precision = 0.01
point_size = 10

canvas = Canvas(root, width=size, height=size)
canvas.pack()

oval = canvas.create_oval(size / 2 - oval_radius, size / 2 - oval_radius, size / 2 + oval_radius,
                          size / 2 + oval_radius, outline="green")


def move_point(start_point, direction="right"):
    global px, py
    print(px)
    if direction == "right":
        x = oval_radius + point_radius * math.cos(start_point)
        y = oval_radius + point_radius * math.sin(start_point)
        print(x, px)
        canvas.move(point, x - px, y - py)
        px, py = x, y
        root.after(speed, move_point, start_point + precision)
    elif direction == "left":
        x = oval_radius + point_radius * math.cos(start_point)
        y = oval_radius + point_radius * math.sin(start_point)
        canvas.move(point, x - px, y - py)
        px, py = x, y
        root.after(speed, move_point, start_point + precision)
    else:
        raise Exception(f"Not valid direction \"{direction}\". Should be \"right\" or \"left\"")


px = -(point_radius / 2 - point_size / 2)
py = -(point_radius / 2 - point_size / 2)
point = canvas.create_oval(0, 0, point_size, point_size, fill='green')
move_point(start_point=math.pi, direction="left")

root.mainloop()
