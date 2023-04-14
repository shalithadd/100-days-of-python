from turtle import Turtle

COLOURS = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

