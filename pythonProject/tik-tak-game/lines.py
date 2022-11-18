from turtle import Turtle

LINE_CO = [(180, 70), (180, -70), (70, -180), (-70, -180)]
HEADING = [180, 180, 90, 90]
MOVE = 360


class Line:
    def __init__(self):
        self.new_line = []

    def create_line(self):
        for num in range(4):
            rio = Turtle()
            rio.speed("normal")
            rio.hideturtle()
            rio.penup()
            rio.pensize(5)
            self.new_line.append(rio)
            self.new_line[num].goto(LINE_CO[num])
            self.new_line[num].pendown()
            self.new_line[num].setheading(HEADING[num])
            self.new_line[num].forward(MOVE)
