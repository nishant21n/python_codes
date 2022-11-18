import turtle
from turtle import Turtle, Screen
from random import randint

rio = Turtle()
turtle.colormode(255)
rio.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
     for i in range(int(360 / size_of_gap)):
        rio.color(random_color())
        rio.circle(100)
        current_heading = rio.heading()
        rio.setheading(current_heading + size_of_gap)

draw_spirograph(7)

screen = Screen()
screen.exitonclick()
