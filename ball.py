from turtle import Turtle 


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move =10
        self.x_move=10
        self.move_speed = 0.1
       
    def r_update(self):
    
        xcor = self.xcor()+self.x_move
        ycor = self.ycor()+self.y_move
        self.goto(xcor,ycor)

    def y_bounce(self):
        self.y_move *= -1
    def x_bounce(self):
        self.x_move*=-1
        self.move_speed  *= 0.9
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.x_bounce()

