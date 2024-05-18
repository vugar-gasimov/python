from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.setheading(45)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        print("class ball", self.x_move, self.y_move)
    def move(self):
        # self.forward(20)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        print("move", self.x_move, self.y_move)
        
    def bounce_y(self):
     self.y_move *= -1
     print("bounce y", self.x_move, self.y_move)
    
    def bounce_x(self):
        self.x_move *= -1
        print("bounce x", self.x_move, self.y_move)
    
    def reposition(self):
        self.goto(0, 0)
        
    def change_direction(self):
        self.x_move *= -1
        # Or bounce_x()
    # def up_right_hit(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() - 10
        # self.goto(x=new_x, y=new_y)
        # self.setheading(315)
    # def up_left_hit(self):
    #     self.setheading(225)
    
    # def down_right_hit(self):
    #     self.setheading(45)
        
    # def down_left_hit(self):
    #     self.setheading(135)