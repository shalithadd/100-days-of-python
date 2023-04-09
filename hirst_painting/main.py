from rbg_colours import colour_list
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
tim.penup()

# Set the starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100

for dot_count in range(1, numbers_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
    # Set start position after drawing 10 dots
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
