from turtle import Turtle, Screen
import heroes
print(heroes.gen())
tim = Turtle()
tim.shape("turtle")
tim.color("green")
for _ in range(4):
    tim.right(90)
    tim.forward(100)
    
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)


screen = Screen()
screen.exitonclick()