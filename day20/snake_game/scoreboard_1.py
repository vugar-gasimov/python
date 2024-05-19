from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("gold")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.speed("fastest")
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
            
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=('Courier', 24, 'bold'))
        
    def increase_score(self):
        self.score += 1
        self.update_score()