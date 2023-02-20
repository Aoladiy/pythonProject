# import time
# from tkinter import *
# from tkinter import colorchooser
# from random import *
#
# size = 600
# root = Tk()
# canvas = Canvas(root, width=size, height=size)
# canvas.focus_set()
# canvas.pack()
#
# oval = canvas.create_oval(size / 2 - 200, size / 2 - 200, size / 2 + 200, size / 2 + 200)
# ball = canvas.create_oval(size / 2 - 20, size / 2 - 200, size / 2 + 20, size / 2 - 160, fill='green')
# x_set = [i for i in range(int(size / 2) - 200, int(size / 2) + 201)]
# print(x_set)
# y_set = [i for i in range(int(size / 2) - 200, int(size / 2) + 201)]
# #print(y_set)
# i = 0
# while True:
#     print(i)
#     #time.sleep(0.1)
#     x_t = x_set[i % len(x_set)]
#     y_t = y_set[i % len(y_set)]
#     if i > len(x_set) / 2:
#         canvas.move(ball, 1, 1)
#     i += 1
#     if i == len(x_set):
#         i = 0
#     root.update()
#
# root.mainloop()

# import tkinter as tk
# import math
#
# # Определяем глобальные переменные для радиуса окружности и скорости движения
# radius = 200
# speed = 1
#
#
# def move_point():
#     global x, y, speed, angle
#     # Вычисляем новые координаты точки
#     x = 300 + int(radius * math.cos(angle))
#     y = 300 + int(radius * math.sin(angle))
#     # Увеличиваем значение угла на скорость движения
#     angle += speed * math.pi / 180
#     # Перерисовываем точку на новых координатах
#     canvas.delete("point")
#     canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", tags="point")
#     # Запускаем функцию снова через 10 миллисекунд
#     root.after(10, move_point)
#
#
# # Создаем главное окно и область для рисования
# root = tk.Tk()
# root.geometry("600x600")
# canvas = tk.Canvas(root, width=600, height=600)
# canvas.pack()
#
# # Рисуем окружность по центру
# canvas.create_oval(100, 100, 500, 500, outline="black")
#
# # Устанавливаем начальные значения координат и угла
# x = 300 + radius
# y = 300
# angle = 0
#
# # Рисуем начальную точку
# canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", tags="point")
#
# # Запускаем функцию движения точки
# move_point()
#
# # Запускаем главный цикл программы
# root.mainloop()

from tkinter import *
import math

root = Tk()
root.geometry('600x600')

canvas = Canvas(root, width=400, height=400)
canvas.pack()

canvas.create_oval(100, 100, 500, 500, outline='black')

def move_point(angle):
    global px, py
    x = 200 + 200 * math.cos(angle)
    y = 200 + 200 * math.sin(angle)
    canvas.move(point, x - px, y - py)
    px, py = x, y
    root.after(10, move_point, angle + 0.01)

px = 0
py = 0
point = canvas.create_oval(0, 0, 10, 10, fill='red')
move_point(0)

root.mainloop()


