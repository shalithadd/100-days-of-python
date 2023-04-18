from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 10, 'normal')


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def populate_map(self, position, state):
        self.goto(position)
        self.write(arg=state, align=ALIGNMENT, font=FONT)
