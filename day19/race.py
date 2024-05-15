from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
# tim.shape("turtle")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
tim.color("green")
screen = Screen()
screen.setup(width = 800, height = 400)
tim.penup()
tim.hideturtle()
tim.pencolor("black")
tim.goto(x=340, y=160)
tim.pendown()
tim.goto(x=340, y=-160)
tim.penup()
tim.goto(x=320, y=160)
tim.pendown()
tim.goto(x=320, y=-160)
tim.penup()
tim.goto(x=-380, y=-160)
race_is_on = False
tim.pendown()
# tim.showturtle()
tim.speed(15)
user_bet = screen.textinput(title= "Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
start_position = -380
start_line = -140
all_turtles = []
for color in colors:
    random_speed = random.randint(1, 8)
    new_turtle = Turtle(shape="turtle")
    new_turtle.hideturtle()
    new_turtle.speed(random_speed)
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=start_position, y= start_line)
    start_line += 55
    all_turtles.append(new_turtle)
    new_turtle.showturtle()
    # new_turtle.forward(760)
if user_bet:
    race_is_on = True
    
while race_is_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 300:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The winning turtle is  {winning_turtle}!.")
            else:
                print(f"You've lost! The winning turtle is {winning_turtle}!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
screen.exitonclick()