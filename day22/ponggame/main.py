from turtle import Screen, Turtle
from paddle import Paddle
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
screen.onkey(r_paddle.r_up, "Up")
screen.onkey(r_paddle.r_down, "Down")
screen.onkey(l_paddle.l_up, "W")
screen.onkey(l_paddle.l_down, "S")

while game_is_on:
    screen.update()
#     if paddle.ycor() < -200:
#         pass
#     elif paddle.ycor() > 200:
#         pass
#     else:
#         paddle.forward(20)














screen.exitonclick()