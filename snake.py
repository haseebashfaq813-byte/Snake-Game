import turtle
DISTANCE = 20
STARTING_POINTS = [(0,0),(-20,0),(-40,0)]

class Snake:
     # attribute segment
    def __init__(self):
        self.segments = []
     # get hold of the position provided in the argument and make a white box there
    def add_segment(self, position):
            jhon = turtle.Turtle('square')
            jhon.color("white")
            jhon.penup()
            jhon.goto(position)
            self.segments.append(jhon)
     # loop through starting points
     # add segment by calling add_segment method
    def start(self):
        for x in STARTING_POINTS:
            self.add_segment(x)
     # method to add segment at position -1 because in a list is last element
    def extend(self):
        self.add_segment(self.segments[-1].position())

     # list starts as [0,1,2] , but snake goes to [2,1,0]
    def move(self):
         # start from 2 , find x and y coordinates of 1 , makes 2 to goto 1 , then 0 goes 20 paces
        for y in range(len(self.segments) - 1, 0, -1):
            xcord = self.segments[y - 1].xcor()
            ycord = self.segments[y - 1].ycor()
            self.segments[y].goto(xcord, ycord)
        self.segments[0].forward(DISTANCE)

     # basic functions to make the snake move by changing angles
     #-----------------------------------------------------------------------
    def go_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)

    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    #--------------------------------------------------------------------------