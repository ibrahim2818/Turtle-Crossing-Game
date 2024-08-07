import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car= CarManager()
level= Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()

    car.create_car()
    car.move_car()
    # for cars in car.all_cars:
    #     if cars.distance(player)<20:
    #         level.game_over()
    #         game_is_on = False
            
    if player.ycor()>280:
        player.goto(0, -280)
        SLEEP_TIME= SLEEP_TIME*0.8
        level.increase()
 
screen.exitonclick()