from turtle import Turtle, Screen
from lines import Line
from user_input import Brain


screen = Screen()
screen.setup(700, 500)

line = Line()
line.create_line()

inputs = Brain()
inputs.circles()

game_is_on = True

inputs.user_key_press()
inputs.computer()


screen.exitonclick()