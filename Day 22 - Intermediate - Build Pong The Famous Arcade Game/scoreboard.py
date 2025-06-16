from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Left: {self.score_l} Right: {self.score_r}", align="center", font=("Courier", 24, "normal"))

    def increase_left_score(self):
        self.score_l += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.score_r += 1
        self.update_scoreboard()