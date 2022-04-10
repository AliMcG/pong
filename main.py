from turtle import Screen
from paddle import Paddle, PLAYER_1_START, PLAYER_2_START
from ball import Ball, START_POS
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(PLAYER_1_START)
paddle_2 = Paddle(PLAYER_2_START)
ball = Ball(START_POS)

screen.listen()
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
