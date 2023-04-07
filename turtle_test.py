from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
my_screen = Screen()
my_screen.colormode(255)

# for _ in range(50):
#     tim.forward(5)
#     if tim.isdown():
#         tim.penup()
#     else:
#         tim.pendown()


# draw shapes
def draw_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


# generate random rgb colour
def generate_random_pen_colour():
    pen_colour = []
    for i in range(3):
        pen_colour.append(random.randint(1, 255))
    return tuple(pen_colour)


for i in range(3, 11):
    tim.pencolor(generate_random_pen_colour())
    draw_shapes(i)


my_screen.exitonclick()
