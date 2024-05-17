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
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
        self.head.shape("triangle")
        self.head.color("green")
      
        # self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
       
            
    def add_segment(self, position):    
        new_segment = Turtle("circle")
        new_segment.speed("slow")
        new_segment.color("LightGreen")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
      
            
    def extend(self):
        # Add new segment to the snake.
        self.add_segment(self.segments[-1].position())
        
        
   
            
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
        
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num -1].xcor()
            new_y = self.segments[segment_num -1].ycor()
            self.segments[segment_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
        # segments[0].left(20)    

        