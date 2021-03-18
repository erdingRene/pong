from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scourboard

import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
scoreboard = Scourboard()
screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(paddle_r) < 55 and ball.xcor() > 320 or ball.distance(paddle_l) < 55 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect when the ball misses the paddle_r
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.point_for_l()

    # Detect when the ball misses the paddle_l
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.point_for_r()
screen.exitonclick()
