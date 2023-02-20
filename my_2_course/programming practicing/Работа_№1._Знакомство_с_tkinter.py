import time
from tkinter import *
from tkinter import colorchooser
from random import *

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.focus_set()
canvas.pack()

oval = canvas.create_oval(size / 2 - 200, size / 2 - 200, size / 2 + 200, size / 2 + 200)
ball = canvas.create_oval(size / 2 - 20, size / 2 - 200, size / 2 + 20, size / 2 - 160, fill='green')
x_set = [i for i in range(int(size / 2) - 200, int(size / 2) + 201)]
print(x_set)
y_set = [i for i in range(int(size / 2) - 200, int(size / 2) + 201)]
#print(y_set)
i = 0
while True:
    print(i)
    #time.sleep(0.1)
    x_t = x_set[i % len(x_set)]
    y_t = y_set[i % len(y_set)]
    if i > len(x_set) / 2:
        canvas.move(ball, 1, 1)
    i += 1
    if i == len(x_set):
        i = 0
    root.update()

root.mainloop()
