from turtle import Screen
from paddles import Paddle
from pongball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)


r_paddle = Paddle(-360, 0)
l_paddle = Paddle(360, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "s")



game_on =True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.movement()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle)<50 and ball.xcor() < -320:
        ball.bouncex()

    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()

screen.exitonclick()