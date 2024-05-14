from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
screen = Screen()
tim.speed(15)

def move_forwards():
    tim.forward(20)
    
def move_right():
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    tim.left(20)
    
def move_backwards():
    tim.backward(20)
    
def move_left():
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    tim.right(20)
    
def clear_screen():
    tim.clear()
    
    
screen.listen()
screen.onkey(key="w", fun = move_forwards)
screen.onkey(key="s", fun = move_backwards)
screen.onkey(key="a", fun = move_right)
screen.onkey(key="d", fun = move_left)
screen.onkey(key="c", fun = clear_screen)

screen.exitonclick()
