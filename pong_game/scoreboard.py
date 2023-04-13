from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 50, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)

    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()
