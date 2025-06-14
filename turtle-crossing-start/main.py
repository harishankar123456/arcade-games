import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
scoreboard =Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
aama = Player()
car_manager = CarManager()
game_is_on = True
screen.listen(),
screen.onkeypress(aama.up,"Up")
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()
    screen.update()
    if aama.is_at_finish_line():
        aama.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()
    for car in car_manager.all_cars:
        if car.distance(aama)<20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()