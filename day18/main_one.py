# from turtle import Turtle, Screen
import turtle as t
import heroes
import random
print(heroes.gen())

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed(25)
tim.pensize(5)
t.colormode(255)

def random_color():
    r = random.randint(10, 245)
    g = random.randint(10, 245)
    b = random.randint(10, 245)
    
    my_color = (r, g, b)
    return my_color
# colors = ["blue",
# "red",
# "darkMagenta",
# "crimson",
# "darkSlateBlue",
# "blue",
# "red",
# "darkMagenta",
# "crimson",
# "darkSlateBlue"]
# directions = ["forward", "right", "backward", "left", ]
# directions = [0, 90, 180, 270]
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        
draw_spirograph(5)
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# def draw_random_walk(num_sides):
#     for _ in range(num_sides):
#         tim.forward(25)
#         random_direction = random.choice(direction)
#         tim.pencolor(random.choice(colors))
#         direction_map = {
#             "forward": tim.forward,
#             "right": tim.right,
#             "down": tim.down,
#             "left": tim.left,
#         }
#         direction_map[random_direction](50)
    
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
# tim.penup()
# tim.left(90)
# tim.forward(250)
# tim.right(90)
# tim.pendown()
# if (-300 < tim.xcor() <300) and (-300 < tim.ycor() <300):
#     for _ in range(100):
#         random_direction = random.choice(direction)
#         tim.pencolor(random.choice(colors))
#         direction_map = {
#             "forward": tim.forward,
#             "right": tim.right,
#             "backward": tim.backward,
#             "left": tim.left,
#             }
#         direction_map[random_direction](90)
    
# draw_random_walk(100)

# Turtle.done()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
        
# for shape_side in range(3, 15):
#     tim.pencolor(random.choice(colors))
#     draw_shape(shape_side)
# tim.pencolor("blue")
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#     tim.forward(100)


# tim.pencolor("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)

    
# tim.pencolor("darkMagenta")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#     tim.forward(100)

# tim.pencolor("crimson")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#     tim.forward(100)
   
# tim.pencolor("darkSlateBlue")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.5)
#     tim.forward(100)
   
# tim.pencolor("blue")
# for _ in range(3):
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     tim.right(120)
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()

# tim.pencolor("red")
# for _ in range(4):
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     tim.right(90)
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
    
# tim.pencolor("dark magenta")
# for _ in range(5):
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     tim.right(72)
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
# tim.pencolor("crimson")
# for _ in range(6):
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     tim.right(60)
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
# tim.pencolor("dark slate blue")
# for _ in range(7):
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     tim.right(51)
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
    # You can use the turtle.penup() and turtle.pendown() methods, to control when the turtle will draw on the canvas and when it won't. Here is the code:
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)


screen = t.Screen()
screen.exitonclick()