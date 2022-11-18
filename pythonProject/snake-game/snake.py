from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def add_square(self, position):
        rio = Turtle("square")
        rio.color("white")
        rio.penup()
        rio.goto(position)
        self.squares.append(rio)

    def reset(self):
        for sqr in self.squares:
            sqr.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        # add new square to the snake body
        self.add_square(self.squares[-1].position())

    def move(self):
        for sq_num in range(len(self.squares) - 1, 0, -1):  # range(start=2, stop=0, step=-1), check in written notes
            new_x = self.squares[sq_num - 1].xcor()  # for x coordinates
            new_y = self.squares[sq_num - 1].ycor()  # for y coordinates
            self.squares[sq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
