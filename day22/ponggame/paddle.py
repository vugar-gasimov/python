from turtle import Turtle

PADDLE_W = 1.0
PADDLE_H = 5.0
X_POS = 350
Y_POS = 0
UP = 90
DOWN = 270
STARTING_POSITIONS = [(-350, 0), (350, 0)]
MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle("square")
        self.paddle.goto(position)
        self.positions= []
        self.positions.append(position)
        self.l_paddle = self.positions[0]
        self.r_paddle = self.positions[1]
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup() 

        
        
        # self.move()
        
        # def move(self):
        #     if self.ycor() < -280:
        #         self.setheading(90)
        #     elif self.ycor() > 280:
        #         self.setheading(270)
        #     self.forward(10)
        
        
    # def create_paddle(self):
    #     for paddle in STARTING_POSITIONS:
    #         new_paddle = Turtle("square")
    #         new_paddle.penup() 
    #         new_paddle.speed("fastest")  
    #         new_paddle.speed("slow")
    #         new_paddle.color("white")
    #         new_paddle.setheading(90) 
    #         new_paddle.shapesize(stretch_wid=PADDLE_W, stretch_len=PADDLE_H)
    #         self.paddles.append(new_paddle)
        
    def r_up(self):
        new_y = self.r_paddle.ycor() + 20
        self.r_paddle.goto(new_y)
          
    def r_down(self):
        new_y = self.r_paddle.ycor() - 20
        self.r_paddle.goto(new_y)
        
    def l_up(self):
        new_y = self.l_paddle.ycor() + 20
        self.l_paddle.goto(new_y)
          
    def l_down(self):
        new_y = self.l_paddle.ycor() - 20
        self.l_paddle.goto(new_y)
        
    # def move(self):
    #     if self.paddles[1].ycor() < -200:
    #         pass
    #     elif self.paddles[1].ycor() > 200:
    #         pass
    #     else:
    #         self.paddles[1].forward(MOVE_DISTANCE)
        