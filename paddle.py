from turtle import Turtle
PLAYER_1_START = (-350, 0)
PLAYER_2_START = (350, 0)


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        position = start_pos
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def up(self,):
        top_edge = self.ycor()
        if top_edge <= 180:
            pp = self.pos()
            self.goto(pp[0], pp[1] + 20)

    def down(self):
        bottom_edge = self.ycor()
        if bottom_edge >= -180:
            pp = self.pos()
            self.goto(pp[0], pp[1] - 20)
