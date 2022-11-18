from turtle import Turtle

FONT = ("Arial", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}\nLevel:{self.level}", align="left", font=FONT)

    def score_update(self):
        self.clear()
        self.score += 10
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
