from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")

game_is_on = True 

screen.tracer(0)

r_paddle = Paddle((380,0))
l_paddle = Paddle((-387,0))

screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")
ball = Ball()
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
  
    ball.r_update()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()
    if ball.xcor()>325 and ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50 and ball.xcor()<-325 :
        ball.x_bounce()

    if ball.xcor()>400:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()