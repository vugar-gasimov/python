from turtle import Turtle
START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_Y_LINE = -280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.setheading(90)
        self.reposition()
        self.shape("turtle")
        
    # def move(self):
    #     self.forward(MOVE_DISTANCE)
        
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE    
        self.goto(x=self.xcor(), y=new_y)
        
    def reposition(self):
        self.goto(START_POSITION)