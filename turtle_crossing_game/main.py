from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key='Up', fun=player.go_up)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player reached the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increment_level()
        car_manager.speed_up()

screen.exitonclick()
