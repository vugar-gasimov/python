from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180
# snake = Turtle()
# snake.setheading()
class Snake:
    
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.tail = self.snakes[-1]
        self.head.shape("triangle")
        self.head.color("green")
        self.tail.shapesize(0.7, 0.7)
        # self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle("circle")
            new_snake.speed("slow")
            new_snake.color("LightGreen")
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)
            
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
        
    def move(self):
        
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num -1].xcor()
            new_y = self.snakes[snake_num -1].ycor()
            self.snakes[snake_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
        # snakes[0].left(20)    

        