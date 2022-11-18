import time
import turtle
from turtle import Screen
from cars import CarManager
from game_turtle import RioTurtle
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.title("iNNK.Turtle_Crossing_v1.0")
screen.tracer(0)
turtle.colormode(255)

car_manager = CarManager()
rio_turtle = RioTurtle()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(rio_turtle.move_fw, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(rio_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if rio_turtle.is_at_finish_line():
        rio_turtle.go_to_start()
        car_manager.level_up()
        scoreboard.score_update()


screen.exitonclick()

