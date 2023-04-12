from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)
screen.onkey(key='Up', fun=r_paddle.go_up)
screen.onkey(key='Down', fun=r_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

screen.exitonclick()
