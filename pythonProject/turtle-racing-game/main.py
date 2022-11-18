from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.bgpic('bg.gif')
screen.update()
screen.setup(width=500, height=400)
colors = ["red", "yellow", "black", "green", "blue", "purple"]
all_turtles = []
new_t = -75

for turtle_index in range(6):
    rio = Turtle("turtle")
    rio.penup()
    rio.color(colors[turtle_index])
    rio.goto(-230, new_t)
    new_t += 30
    all_turtles.append(rio)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
               a = screen.textinput("Winner!", f"You have won!! The {win_color} turtle is the Winner!!")
               if a != " ":
                   screen.clear()
            else:
               b = screen.textinput("!!You have lost!!", f"The {win_color} turtle is the Winner.")
               if b != " ":
                   screen.clear()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        """turtle is used means its Instane
                  Object = Class
        Instance  rio = Turtle()
        Instance  mio = Turtle()"""


screen.exitonclick()
