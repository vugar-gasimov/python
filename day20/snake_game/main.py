from turtle import Screen, Turtle
import time
snake_length = 3
body_x=0
body_y=0
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("darkBlue")
screen.title("Snake Game")
screen.tracer(0)

# snake = Turtle(shape="circle")
# snake.shapesize(1, 1, 1)
# snake.color("darkGreen")
bodies = []
for _ in range(0, snake_length + 1):
    new_body =Turtle(shape="circle")
    new_body.penup()
    new_body.shapesize(1, 1, 1)
    new_body.color("lightGreen")
    new_body.goto(x=body_x,y=body_y)
    body_x -= 20
    bodies.append(new_body)

 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    for body_num in range(len(bodies) - 1, 0, -1):
        new_x = bodies[body_num - 1].xcor()
        new_y = bodies[body_num - 1].ycor()
        bodies[body_num].goto(x=new_x, y=new_y)
        
    bodies[0].forward(20)
    bodies[0].left(20)
    # for body in bodies:
    #     body_x += 20
    #     body.goto(x=body_x,y=body_y)











screen.exitonclick()