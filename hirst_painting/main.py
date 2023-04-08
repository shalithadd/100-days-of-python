from rbg_colours import colour_list
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
tim.penup()

colour = (random.choice(colour_list))


def fill_circle(random_colour):
    tim.color(random_colour, random_colour)
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()


fill_circle(colour)

screen.exitonclick()
