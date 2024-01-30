from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align="center", font="Arial 20 normal")
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font="Arial 20 normal")

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GÀ VCL LUÔN Á", align="center", font="Arial 34 normal")