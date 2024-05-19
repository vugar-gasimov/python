from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("gray")
screen.tracer(0)


game_on = True
road = Road()
# road.draw_road()
# road.draw_sidelines()

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")


while game_on:
    time.sleep(score.move_speed)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars()
    
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_on = False
            score.game_over()
            
    if player.ycor() > 250:
        player.reposition()
        score.increase_score()
        
        



















screen.exitonclick()