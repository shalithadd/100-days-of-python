from turtle import Screen
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(key='Up', fun=player.up)

game_is_on = True
count = 6
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if count % 6 == 0:
        car_manager.new_car()
    car_manager.move_car()
    count += 1

