import random
import math


class Boid:
    def __init__(self, label):
        self.x = random.randrange(100, 900)
        self.y = random.randrange(100, 900)
        self.angle = random.uniform(0.0, 2.0 * math.pi)
        self.label = label
        self.color = "black"

    def draw_boid(self, canvas):
        size = 18
        x1 = self.x + size * math.cos(self.angle)
        x2 = self.y + size * math.sin(self.angle)
        canvas.create_line(self.x, self.y, x1, x2, fill='gray', arrow='last', arrowshape=(12.8, 16, 4.8), width=2,
                           tags=self.label)

    def flock(self, canvas, screen_size):
        distance = 30

        self.x += distance * math.cos(self.angle)
        self.y += distance * math.sin(self.angle)

        self.x = self.x % screen_size
        self.y = self.y % screen_size
        canvas.delete(self.label)
        self.draw_boid(canvas)

    def euclidean_distance(self, neighbour_boid):
        return math.sqrt((self.x - neighbour_boid.x) ** 2 + (self.y - neighbour_boid.y) ** 2)
