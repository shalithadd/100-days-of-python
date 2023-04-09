from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_game_on = False
user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? enter a colour: ')
print(user_bet)
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_cord = -100
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_cord)
    all_turtles.append(new_turtle)
    y_cord += 42

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_colour = turtle.pencolor()
            if user_bet == winning_colour:
                print(f'You won!, The {winning_colour} turtle is the winner.')
            else:
                print(f'You lost!, The {winning_colour} turtle is the winner.')
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
