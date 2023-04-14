from turtle import Turtle
import random

COLOURS = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []

    def new_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLOURS))
        new_car.goto(300, random.randint(-240, 240))
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)



