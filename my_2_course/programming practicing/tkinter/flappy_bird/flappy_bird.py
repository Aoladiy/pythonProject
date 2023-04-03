import random
import tkinter as tk

# Создаем главное окно
root = tk.Tk()

# Задаем размер окна
root.geometry("400x400")

# Добавляем название игры
root.title("Flappy Bird")

# Создаем фоновый цвет
canvas = tk.Canvas(root, width=400, height=400, bg="sky blue")
canvas.pack()

# Создаем птицу
bird = canvas.create_oval(50, 200, 70, 220, fill="white")

# Задаем скорость птицы
bird_speed = 0


# Генерируем препятствия
class Obstacle:
    def __init__(self):
        self.color = "green"

        # Создаем верхнее препятствие
        top_height = random.randint(50, 200)
        self.top = canvas.create_rectangle(400, 0, 350, top_height, fill=self.color)

        # Создаем нижнее препятствие
        bottom_height = random.randint(50, 200)
        self.bottom = canvas.create_rectangle(400, 400, 350, 400 - bottom_height, fill=self.color)

    def collision(self):
        canvas.itemconfig(self.top, fill="red")
        canvas.itemconfig(self.bottom, fill="red")


# Обработка нажатия клавиши
def on_key_press(event):
    global bird_speed
    bird_speed = -10


# Функция движения птицы и препятствий
def move(obstacle):
    global bird_speed
    # Двигаем птицу
    if max(canvas.coords(bird)[1], canvas.coords(bird)[3]) <= 400 or bird_speed < 0:
        canvas.move(bird, 0, bird_speed)
        bird_speed += 1

    # Двигаем препятствия
    canvas.move(obstacle.top, -5, 0)
    canvas.move(obstacle.bottom, -5, 0)

    # Проверяем столкновение с препятствиями
    if canvas.bbox(bird)[0] < canvas.bbox(obstacle.top)[2] \
            and canvas.bbox(bird)[2] > canvas.bbox(obstacle.top)[0] \
            and (canvas.bbox(bird)[1] < canvas.bbox(obstacle.top)[3]
                 or canvas.bbox(bird)[3] > canvas.bbox(obstacle.bottom)[1]):
        obstacle.collision()

    # Генерируем новые препятствия при необходимости
    if canvas.bbox(obstacle.top)[2] < 0:
        canvas.delete(obstacle.top)
        canvas.delete(obstacle.bottom)
        obstacle = Obstacle()

    # Запускаем функцию снова через 25 миллисекунд
    canvas.after(25, move, obstacle)


# Привязываем обработчик нажатия клавиши к событию нажатия клавиши
canvas.bind_all('<space>', on_key_press)

# Запускаем игру
# Задаем начальное препятствие
obstacle = Obstacle()
move(obstacle)

# Запускаем главный цикл обработки событий
root.mainloop()
