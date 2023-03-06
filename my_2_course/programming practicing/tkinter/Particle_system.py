import tkinter as tk
import random
import numpy as np

WIDTH = 400
HEIGHT = 400

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

# Создаем список цветов для имитации пламени огня
colors = ['#ff9933', '#ff6600', '#ff3300', '#cc0000', '#990000']


# colors = ['red', 'orange']


# Создаем класс Particle для имитации каждой частицы огня
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(colors)
        self.size = random.randint(5, 10)
        self.life = random.randint(5, 25)

        def speed():  # Определяем направление движения
            while True:
                y_speed = -abs(np.random.laplace()) * 2
                x_speed = np.random.laplace()
                if y_speed / x_speed > 2:
                    if np.random.randint(0, 2) == 0:
                        return y_speed, x_speed
                    else:
                        return y_speed, -x_speed  # Зеркалим
                else:
                    continue

        self.y_speed, self.x_speed = speed()

    def move(self):
        self.y += self.y_speed
        self.x += self.x_speed
        self.life -= 1

    def draw(self):
        canvas.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size,
                           fill=self.color, outline='', tags='particle')


# Создаем функцию для генерации новых частиц
def generate_particles(x, y):
    canvas.delete('particle')

    # Удаляем "мертвые" частицы
    particles[:] = [p for p in particles if p.life > 0]

    # Генерируем новые частицы
    for _ in range(random.randint(5, 20)):
        particle = Particle(x / 2, y)
        particle.draw()
        particles.append(particle)

    # Двигаем все частицы
    for particle in particles:
        particle.move()
        particle.draw()

    # Запускаем функцию еще раз через небольшой интервал времени
    canvas.after(20, generate_particles, coords[-1][0], coords[-1][1])


# Создаем список для хранения частиц огня
particles = []

coords = []


def getxy(event):
    coords.append((event.x, event.y))
    generate_particles(*coords[-1])


root.bind('<ButtonPress-1>', getxy)

# Запускаем генерацию частиц
# generate_particles()

root.mainloop()
