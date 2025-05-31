from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setpos(position)
        self.speed("fastest")
        self.shapesize(stretch_len=1,stretch_wid=5)

    def up(self):
        ycor = self.ycor()
        new_y = ycor + 20  
        self.goto(self.xcor(),new_y)
        
    def down(self):
        ycor = self.ycor()
        new_y = ycor - 20
        self.goto(self.xcor(),new_y)