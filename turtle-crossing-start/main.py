import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
adam = Player()
car_manager = CarManager()
game_is_on = True
screen.listen(),
screen.onkeypress(adam.up,"Up")
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()
    screen.update()
