from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)


def random_colour():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    colour = (r, g, b)
    return colour


tim.hideturtle()
tim.speed("fastest")


def draw_spirograph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        tim.setheading(tim.heading() + size_of_the_gap)
        tim.color(random_colour())
        tim.circle(70)


draw_spirograph(5)
screen.exitonclick()
