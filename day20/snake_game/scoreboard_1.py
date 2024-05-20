from turtle import Turtle
# r_data = open("day20\snake_game\data.txt", mode="r")
# w_data = open("day20\snake_game\data.txt", mode="w")
# data_high_score = r_data.read()
# print(data_high_score)
# with open("snake_game\data.txt", mode="r") as data:
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("gold")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.high_score = self.read_high_score()
        self.speed("fastest")
        self.update_score()
        
    def read_high_score(self):
        with open("day20\snake_game\data.txt", mode="r") as data:
            # self.high_score = int(data.read())
            high_score_str = data.read().strip()
            if high_score_str.isdigit():
                return int(high_score_str)
            else:
                return 0
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score    
            with open("day20\snake_game\data.txt", mode="w") as data:
                # data.write(str(self.high_score))
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
            
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=('Courier', 24, 'bold'))
        
    def increase_score(self):
        self.score += 1
        self.update_score()