from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)


def walk_random(walk_distance, turn_angle):
    distance = walk_distance
    angle = turn_angle
    directions = random.choice([tim.forward, tim.backward])
    turns = random.choice([tim.right, tim.left])
    walk = directions(distance), turns(angle)
    return walk


def random_pencolour():
    new_colour = []
    for i in range(3):
        new_colour.append(random.randint(1, 255))
    return tuple(new_colour)


tim.hideturtle()
tim.pensize(15)
tim.speed(10)
while True:
    tim.pencolor(random_pencolour())
    walk_random(30, 90)
screen.exitonclick()
