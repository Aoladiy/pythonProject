import random
import tkinter as tk

# Скорость птицы
bird_speed = 0
# Плотность труб от 50 до 400
pipe_density = 200
# Размер окна
window_size = 400

root = tk.Tk()
root.geometry(f"{window_size}x{window_size}")
root.title("Flappy Bird")

canvas = tk.Canvas(root, width=window_size, height=window_size, bg="sky blue")
canvas.pack()


class Obstacle:
    def __init__(self):
        self.color = "green"
        hole_location = random.randint(100, window_size - 100)
        hole_size = 50

        self.top = canvas.create_rectangle(window_size + 50, 0, window_size, hole_location - hole_size, fill=self.color)

        self.bottom = canvas.create_rectangle(window_size + 50, window_size, window_size, hole_location + hole_size,
                                              fill=self.color)

    def in_pipe(self):
        canvas.itemconfig(self.top, fill="red")
        canvas.itemconfig(self.bottom, fill="red")

    def out_pipe(self):
        canvas.itemconfig(self.top, fill="green")
        canvas.itemconfig(self.bottom, fill="green")


def on_key_press(event):
    global bird_speed
    bird_speed = -10


canvas.bind_all('<space>', on_key_press)


def move(obstacles):
    global bird_speed

    if max(canvas.coords(bird)[1], canvas.coords(bird)[3]) <= window_size or bird_speed < 0:
        canvas.move(bird, 0, bird_speed)
        bird_speed += 1

    for obstacle in obstacles:
        canvas.move(obstacle.top, -5, 0)
        canvas.move(obstacle.bottom, -5, 0)

        if canvas.bbox(bird)[0] < canvas.bbox(obstacle.top)[2] \
                and canvas.bbox(bird)[2] > canvas.bbox(obstacle.top)[0] \
                and (canvas.bbox(bird)[1] < canvas.bbox(obstacle.top)[3]
                     or canvas.bbox(bird)[3] > canvas.bbox(obstacle.bottom)[1]):
            obstacle.in_pipe()
        else:
            obstacle.out_pipe()

    if canvas.bbox(obstacle.top)[2] < 0:
        canvas.delete(obstacle.top)
        canvas.delete(obstacle.bottom)
    if canvas.bbox(obstacle.top)[2] < pipe_density:
        obstacles.append(Obstacle())

    canvas.after(25, move, obstacles)


bird = canvas.create_oval(50, 200, 70, 220, fill="white")
obstacles = [Obstacle()]
move(obstacles)

root.mainloop()
