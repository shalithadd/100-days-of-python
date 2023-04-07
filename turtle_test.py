from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# for _ in range(4):
#     tim.backward(100)
#     tim.right(90)
for _ in range(50):
    tim.forward(5)
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()

my_screen = Screen()
my_screen.exitonclick()
