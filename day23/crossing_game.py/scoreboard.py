from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=-230, y=270)
        self.move_speed = 0.1
        # print("speed 1", self.move_speed)
        self.color("gold")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_score()
       
    
    def road(self):
        self.setpos()
    
    def update_score(self):
        # print("speed 2", self.move_speed)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        # self.score += 1
        # self.move_speed *= 0.9
        # print("speed 3", self.move_speed)
        
    def increase_score(self):
        self.score += 1
        self.move_speed *= 0.9
        self.update_score()
        # print("speed 4", self.move_speed)
        
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font="bold")