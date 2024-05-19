from turtle import Turtle

class Road():
    def __init__(self):
        self.road = Turtle("square")
        self.road.penup()
        self.road.goto(x=0, y=0)
        # self.road.pendown()
        self.road.color("black")
       
        self.road.shapesize(stretch_wid=25, stretch_len=50)
        self.sideline = Turtle("square")
        self.sideline.penup()
        self.sideline.goto(x=0, y=0)
        self.sideline.setheading(90)
        self.sideline.color("white")
        self.sideline.shapesize(stretch_wid=30, stretch_len=0.1)
        # self.road.hideturtle()
        # self.draw_sidelines()
       
    # def draw_road(self):   
    #     self.road.width(10)
    #     self.road.shapesize(500)
    #     self.road.setheading(0)
    #     self.road.forward(600) 
        
    # def draw_sidelines(self):
    #     for i in range(2):
    #         sideline=Turtle()
    #         sideline.penup()
    #         sideline.color("white")
    #         sideline.goto(x = -300, y = -250)
    #         sideline.setheading(0)
    #         sideline.pendown()
    #         sideline.forward(600)
    #         sideline.hideturtle()