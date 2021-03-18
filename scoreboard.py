from turtle import Turtle


class Scourboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 200)
        self.write(self.l_score, align="center", font=("Courier", 66, "normal"))
        self.goto(180, 200)
        self.write(self.r_score, align="center", font=("Courier", 66, "normal"))

    def point_for_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def point_for_r(self):
        self.r_score += 1
        self.update_scoreboard()

