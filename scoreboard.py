from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.levels()

    def levels(self):
        self.write(f"Level:{self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.levels()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

