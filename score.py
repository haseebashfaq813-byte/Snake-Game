import turtle

 # using inheritance of turtle class in score class
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

        # make wrting "score " to go to coordinate y = 270 which is top
        self.goto(-10,270)
        self.write(f"SCORE = {self.score}", align="center", font=("Comic Sans MS", 15, "normal"))

     # method to write game over text in the middle of screen
    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER!!", align="center", font=("Comic Sans MS", 15, "bold"))

     # add 1 to score and clear screen and then write score again because if we dont clear then it will overwrite
    def new_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score}", align="center", font=("Comic Sans MS", 15, "normal"))



