from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
# screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

# paddle = Turtle("square")
# # paddle.hideturtle()
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup() 
# # paddle.speed("fastest")  
# paddle.goto(x = 350, y = 0)
# # paddle.showturtle()
# # paddle.speed("slow")
# # paddle.setheading(90)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(x= paddle.xcor(), y=new_y)

# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(x= paddle.xcor(), y=new_y)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    
    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce_y
        ball.bounce_y()
        
        
    
    
    # Detect collisions with right paddle.
    if  ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
        
    # Detect missing the ball.
    # For right side.
    if ball.xcor() > 380:
        # Ball position center and other start moving direction.
        ball.reposition()
        ball.change_direction()
    # For left side.
    if ball.xcor() < - 380:
        ball.reposition()
        ball.change_direction()
    
    # # Detect collisions with left paddle.
    # if ball.xcor() < -380 or ball.distance(l_paddle) < 50:
    #     ball.bounce_x()
    
    
    # Detect collisions with left paddle.
    
    
    
        # ball.up_right_hit()
    # #Detect collision with wall (up left).
    # if ball.ycor() > 300 and ball.xcor() < 0:
    #     ball.up_left_hit()
    # #Detect collision with wall (down right).
    # if  ball.ycor() < -300 and ball.xcor() > 0:
    #     ball.down_right_hit()
    # #Detect collision with wall (down left).
    # if  ball.ycor() < -300 and ball.xcor() < 0:
        # ball.down_left_hit()
        
#     if paddle.ycor() < -200:
#         pass
#     elif paddle.ycor() > 200:
#         pass
#     else:
#         paddle.forward(20)














screen.exitonclick()