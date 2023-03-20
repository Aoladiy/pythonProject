import tkinter
import math
import Boid


def initialise_canvas(root, screen_size):
    canvas = tkinter.Canvas(root, width=screen_size, height=screen_size, background='black')
    canvas.pack()
    root.resizable(False, False)
    return canvas


def create_boids(canvas, number_of_boids):
    list_of_boids = []
    for n in range(number_of_boids):
        boid = Boid.Boid("boid" + str(n))
        list_of_boids.append(boid)
        boid.draw_boid(canvas)
    return list_of_boids


def separation(nearest_neighbour, boid):
    if nearest_neighbour is not None and boid.euclidean_distance(nearest_neighbour) < 35:
        if nearest_neighbour.x - boid.x == 0:
            angle = math.atan((nearest_neighbour.y - boid.y) / 0.0001)
        else:
            angle = math.atan((nearest_neighbour.y - boid.y) / (nearest_neighbour.x - boid.x))
        boid.angle -= angle / 2


def alignment(neighbours, boid):
    average_neighbours_angle = 0
    if neighbours:
        for neighbour_boid in neighbours:
            average_neighbours_angle += neighbour_boid.angle
        average_neighbours_angle /= len(neighbours)
        boid.angle = average_neighbours_angle


def cohesion(neighbours, boid):
    if neighbours:
        avg_x = 0
        avg_y = 0
        for neighbour_boid in neighbours:
            avg_x += neighbour_boid.x
            avg_y += neighbour_boid.y
        avg_x /= len(neighbours)
        avg_y /= len(neighbours)
        if avg_x - boid.x == 0:
            angle = math.atan((avg_y - boid.y) / 0.00001)
        else:
            angle = math.atan((avg_y - boid.y) / (avg_x - boid.x))
        boid.angle -= angle / 20


def boid_behaviours(canvas, list_of_boids, screen_size):
    for boid in list_of_boids:
        neighbours = []
        for b in list_of_boids:
            if boid.euclidean_distance(b) < 75 and (not boid.euclidean_distance(b) == 0):
                neighbours.append(b)
        nearest_neighbour = None
        if neighbours:
            shortest_distance = screen_size
            for neighbour_boid in neighbours:
                distance = boid.euclidean_distance(neighbour_boid)
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_neighbour = neighbour_boid

        separation(nearest_neighbour, boid)
        alignment(neighbours, boid)
        cohesion(neighbours, boid)

    for boid in list_of_boids:
        boid.flock(canvas, screen_size)
    canvas.after(1, boid_behaviours, canvas, list_of_boids, screen_size)


def main():
    screen_size = 900
    number_of_boids = 100
    root = tkinter.Tk()
    canvas = initialise_canvas(root, screen_size)
    list_of_boids = create_boids(canvas, number_of_boids)
    boid_behaviours(canvas, list_of_boids, screen_size)
    root.mainloop()


main()
