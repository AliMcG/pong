from turtle import Turtle

import ball

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.color("white")
        self.track_score()

    def track_score(self):
        self.write(f"Player One: {self.player1_score}   Player Two: {self.player2_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.track_score()
        # self.player1_score += 1
