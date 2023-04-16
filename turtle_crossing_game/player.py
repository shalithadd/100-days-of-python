from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINSH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Rest the player position to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Return true if player is at the finish line."""
        return self.ycor() > FINSH_LINE_Y
