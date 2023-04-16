from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
distance_1 =(350, 0)
distance_2 = (-350, 0)
paddle_1 = Paddle(distance_1)
paddle_2 = Paddle(distance_2)
ball = Ball()
score = Score()
screen.listen()
screen.onkey(fun=paddle_1.move_up, key="Up")
screen.onkey(fun=paddle_1.move_down, key="Down")
screen.onkey(fun=paddle_2.move_up, key="w")
screen.onkey(fun=paddle_2.move_down, key="s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.refresh()
        score.increase_player2()
        time.sleep(1)
    if ball.xcor() < -380:
        ball.refresh()
        score.increase_player1()
        time.sleep(1)













screen.exitonclick()