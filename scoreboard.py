from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level= 1
        self.hideturtle()
        self.goto(-230,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.level}",move= False,align="center", font=FONT)

    def increase(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f" Game Over Level= {self.level} ", move=False, align="center" ,font=FONT)
        
    
