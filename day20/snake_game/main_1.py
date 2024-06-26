from turtle import Screen
from snake_1 import Snake
from food_1 import Food
from scoreboard_1 import Scoreboard
import time
# snake_length = 2
# body_x=-20
# body_y=-0
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("darkBlue")
screen.title("Snake Game")
screen.tracer(0)

# starting_positions = [(0,0), (-20, 0), (-40, 0)]

# snakes=[]
snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left," Left")
# for position in starting_positions:
#     new_snake = Turtle(shape="circle")
#     new_snake.speed("slow")
#     new_snake.color("LightGreen")
#     new_snake.penup()
#     new_snake.goto(position)
#     snakes.append(new_snake)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or  snake.head.ycor() < -280:
        # game_is_on = False
        score.reset_score()
        snake.reset_snake()
        # score.game_over()
    
    # Detect collisions with tail.
    for segment in snake.segments[1:]:
        # if segment  == snake.head:
            # pass
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset_score()
            
            snake.reset_snake()
            # score.game_over()
    
    
    # for snake_num in range(start=2, stop=0, step=-1):
    # for snake_num in range(len(snakes) - 1, 0, -1):
    #     new_x = snakes[snake_num -1].xcor()
    #     new_y = snakes[snake_num -1].ycor()
    #     snakes[snake_num].goto(x=new_x, y=new_y)
    # snakes[0].forward(20)
    # snakes[0].left(20)
    # for snake in snakes:
    #     snake.forward(20)
# snake_1 = Turtle(shape="circle")
# snake_1.color("darkGreen")
# snake_2 = Turtle(shape="circle")
# snake_2.color("darkGreen")
# snake_2.goto(x=-20, y=0)
# snake_3 = Turtle(shape="circle")
# snake_3.color("darkGreen")
# snake_3.goto(x=-40, y=0)

# for _ in range(0, snake_length + 1):
#     new_body =Turtle(shape="circle")
#     new_body.shapesize(1, 1, 1)
#     new_body.color("darkGreen")
    # new_body.goto(x=body_x,y=body_y)
    # body_x += 20
    
    











screen.exitonclick()