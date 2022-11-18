from turtle import Turtle, Screen
import random
import keyboard

POSITION = {
    "a": (0, 0),
    "b": (130, 0),
    "c": (-130, 0),
    "d": (130, 130),
    "e": (0, 130),
    "f": (-130, 130),
    "g": (130, -130),
    "h": (0, -130),
    "i": (-130, -130),
}
SIZE_OF_CIRCLE = 3
key_used = ["0", ]


class Brain:
    def __init__(self):
        self.screen = Screen()
        self.new_circle = []
        self.key = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        self.keyboard = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.status = False
        self.move = 8

    def circles(self):
        for num in range(9):
            rio_circle = Turtle()
            rio_circle.speed("fastest")
            rio_circle.hideturtle()
            rio_circle.penup()
            rio_circle.shape("circle")
            rio_circle.shapesize(SIZE_OF_CIRCLE)
            rio_circle.goto(-250, 0)
            rio_circle.showturtle()
            self.new_circle.append(rio_circle)

    def one(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[8]])
        key_used.append("1")
        self.move -= 1

    def two(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[7]])
        key_used.append("2")
        self.move -= 1

    def three(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[6]])
        key_used.append("3")
        self.move -= 1

    def four(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[2]])
        key_used.append("4")
        self.move -= 1

    def five(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[0]])
        key_used.append("5")
        self.move -= 1

    def six(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[1]])
        key_used.append("6")
        self.move -= 1

    def seven(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[5]])
        key_used.append("7")
        self.move -= 1

    def eight(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[4]])
        key_used.append("8")
        self.move -= 1

    def nine(self):
        (self.new_circle[self.move]).color("red")
        (self.new_circle[self.move]).goto(POSITION[self.key[3]])
        key_used.append("9")
        self.move -= 1

    def user_key_press(self):
        self.screen.listen()
        self.screen.onkey(self.one, self.keyboard[0])
        self.screen.onkey(self.two, self.keyboard[1])
        self.screen.onkey(self.three, self.keyboard[2])
        self.screen.onkey(self.four, self.keyboard[3])
        self.screen.onkey(self.five, self.keyboard[4])
        self.screen.onkey(self.six, self.keyboard[5])
        self.screen.onkey(self.seven, self.keyboard[6])
        self.screen.onkey(self.eight, self.keyboard[7])
        self.screen.onkey(self.nine, self.keyboard[8])

    def computer(self):
        print(key_used[-1])
        if keyboard.read_key() == key_used[-1]:
            random_choice = random.randint(0, 9)
            if random_choice != key_used[-1]:
                (self.new_circle[self.move]).color("black")
                (self.new_circle[self.move]).goto(POSITION[self.key[random_choice]])
                self.move -= 1
        print(key_used)

print(key_used)