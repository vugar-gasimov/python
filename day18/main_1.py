import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(245, 211, 177), (232, 132, 91), (204, 141, 148), (242, 193, 89), (84, 84, 104), (128, 178, 154), (210, 42, 40), (246, 127, 0), (42, 157, 142), (0, 48, 73), (38, 70, 83), (156, 74, 80), (56, 60, 89), (147, 154, 163), (208, 78, 76), (239, 167, 154), (25, 22, 17), (22, 27, 23), (217, 194, 199), (209, 180, 186)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen = t.Screen()
screen.exitonclick()