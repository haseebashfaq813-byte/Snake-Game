import random
import turtle

 #using inheritance of turtle class in food class
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.food_xcor = None
        self.food_ycor = None
        self.shape('circle')
        self.color("red")
        self.shapesize(0.5)
        self.penup()
#----------------------------------------------------------------------

     # makes food appear at a random c=x and y coordinate
    def appear_food(self):
        self.food_xcor = random.randint(-280,280)
        self.food_ycor = random.randint(-280,280)
        self.goto(self.food_xcor,self.food_ycor)
#-------------------------------------------------------------------------



