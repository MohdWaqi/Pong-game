from turtle import Turtle
FONT = ("Arial", 50, "normal")
ALIGNMENT = "center"

################## Setting up the Score Board ######################


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.write(arg=f"{self.player2}  {self.player1}", align=ALIGNMENT, font=FONT)

    def increase_player1(self):
        self.clear()
        self.player1 += 1
        self.write(arg=f"{self.player2}  {self.player1}", align=ALIGNMENT, font=FONT)

    def increase_player2(self):
        self.clear()
        self.player2 +=1
        self.write(arg=f"{self.player2}  {self.player1}", align=ALIGNMENT, font=FONT)



