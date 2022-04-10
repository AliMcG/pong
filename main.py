from turtle import Screen
from paddle import Paddle, PLAYER_1_START, PLAYER_2_START
from ball import Ball, START_POS
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
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

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 337:
        ball.bounce_x()
    if ball.distance(paddle_1) < 49 and ball.xcor() > -341:
        ball.bounce_x()
        # BUG!- the ball bounces on and off the paddle until it clears the paddle.

    if ball.xcor() > 395:
        ball.ht()
        ball = Ball(START_POS)
        ball.bounce_x()
        scoreboard.player1_score += 1
        scoreboard.increase_score()

    if ball.xcor() < -395:
        ball.ht()
        ball = Ball(START_POS)
        scoreboard.player2_score += 1
        scoreboard.increase_score()

screen.exitonclick()
