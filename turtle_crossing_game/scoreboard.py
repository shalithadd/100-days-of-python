from turtle import Turtle

FONT = ('Courier', 17, 'normal')
POSITION = (-230, 260)
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg='Game over!', align=ALIGNMENT, font=FONT)
