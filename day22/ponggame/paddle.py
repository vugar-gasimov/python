from turtle import Turtle

# PADDLE_W = 1.0
# PADDLE_H = 5.0
# X_POS = 350
# Y_POS = 0
# UP = 90
# DOWN = 270
# STARTING_POSITIONS = [(-350, 0), (350, 0)]
# MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup() 
        self.goto(position)

        
    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
          
    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
