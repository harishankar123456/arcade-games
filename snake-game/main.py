from turtle import Screen,Turtle
from food import Food
import snake
import time
from scoreboard import ScoreBoard

#initializing the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)#switch off the animation
scoreboard = ScoreBoard()
snake = snake.Snake()
food = Food()
game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()#switch on the animation
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.grow()
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()