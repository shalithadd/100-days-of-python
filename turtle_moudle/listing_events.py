from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.setheading(0)
    tim.forward(10)


def move_backward():
    tim.setheading(180)
    tim.forward(10)


screen.listen()
screen.onkey(key='d', fun=move_forward)
screen.onkey(key='a', fun=move_backward)
screen.exitonclick()
