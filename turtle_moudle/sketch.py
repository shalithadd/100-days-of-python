from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_anti_clockwise():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='a', fun=turn_anti_clockwise)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
