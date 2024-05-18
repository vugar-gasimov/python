from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self, position, side):
        super().__init__()
        self.goto(position)
        self.color("gold")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_score(side)
       
        
    def update_score(self, side):
        self.clear()
        self.write(f"{side}: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1
        

        