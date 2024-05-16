from turtle import Turtle

class Snake():
    def __init__(self):
        self.snake_length = 3
        self.body_x=0
        self.body_y=0
        self.bodies = []
        
        for _ in range(0, self.snake_length ):
            new_body =Turtle(shape="circle")
            new_body.penup()
            new_body.shapesize(1, 1, 1)
            new_body.color("lightGreen")
            new_body.goto(x=self.body_x,y=self.body_y)
            self.body_x -= 20
            self.bodies.append(new_body)
    
    def up(self):
        if self.bodies[0].heading() != 270:
            self.bodies[0].setheading(90)
        
    def right(self):
        if self.bodies[0].heading() != 180:
            self.bodies[0].setheading(0)
        
        
    def down(self):
        if self.bodies[0].heading() != 90:
            self.bodies[0].setheading(270)
        
        
    def left(self):
        if self.bodies[0].heading() != 0:
            self.bodies[0].setheading(180)
    
    
    def move(self):
        for body_num in range(len(self.bodies) - 1, 0, -1):
            new_x = self.bodies[body_num - 1].xcor()
            new_y = self.bodies[body_num - 1].ycor()
            self.bodies[body_num].goto(x=new_x, y=new_y)
        self.bodies[0].forward(20)
        # self.bodies[0].left(20)