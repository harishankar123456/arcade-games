# create a food class that inherits the Turtle class properties
#turtle is the superclass and super() is the supreclass constructor
from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("Blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
    def refresh(self):
        ran_x = randint(-280,280)
        ran_y = randint(-280,280)
        self.goto(ran_x,ran_y)