from turtle import Turtle
import random
COLORS = ["red", "blue", "yellow", "purple", "orange", "teal"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        # self.create_cars()
        self.loop_counter = 0
        
        
    def create_cars(self):
        # random_car_amount = random.randint(0, 1)
        # for _ in range(random_car_amount):
        self.loop_counter +=1
        # print("Loop", self.loop_counter, "Cars", len(self.cars))
        if self.loop_counter % 6 == 0:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            possible_y_position = [y for y in range(-250, 250, 10) if y not in range(-5, 5)]
            random_y = random.choice(possible_y_position)
            new_car.goto(x=300, y=random_y)
            if new_car.ycor() > 0:
                new_car.goto(-300, new_car.ycor())
            new_car.setheading(180)
            self.cars.append(new_car)
            
            
    def move_cars(self):
        for car in self.cars:
            if car.ycor() > 0:
                # car.setheading(0)
                car.backward(MOVE_INCREMENT) 
            else:
                # car.setheading(180)  
                car.forward(MOVE_INCREMENT) 