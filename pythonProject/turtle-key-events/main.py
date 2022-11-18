from turtle import Turtle, Screen

rio = Turtle()
screen = Screen()


def move_forword():
    rio.forward(10)


def move_backword():
    rio.backward(10)


def move_clockwise():
    rio.right(10)
    rio.forward(10)


def move_counter_clockwise():
    rio.left(10)
    rio.forward(10)


def clear_screen():
    rio.setposition(0, 0)
    rio.setheading(0)
    rio.clear()


screen.listen()
screen.onkey(move_forword, "w")
screen.onkey(move_backword, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()

### Etch-A-Sketch App_by-Me###
