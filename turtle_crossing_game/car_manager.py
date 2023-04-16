from turtle import Turtle
import random

COLOURS = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLOURS))
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
