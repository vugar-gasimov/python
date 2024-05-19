from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

l_scoreboard = Scoreboard((-100, 270), "Left")
r_scoreboard = Scoreboard((100, 270), "Right")
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
    time.sleep(ball.move_speed)
    
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
        l_scoreboard.update_score("Left")

    if ball.xcor() < - 380:
        ball.reposition()
        ball.change_direction()
        r_scoreboard.update_score("Right")

screen.exitonclick()