from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score:{self.score}", align="center", font=('Arial', 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=('Arial', 24, "normal"))
    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
        with open("data.txt",mode='w') as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=('Arial', 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font =('Arial',24,"normal"))