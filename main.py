 # time and turtle default , snake , food , score selfmade
import time
import turtle
import snake
import food
import score

 # games screen , setup of screen
display = turtle.Screen()
display.tracer(0)
display.setup(width=600, height=600)
display.title("THE SNAKE GAME")
display.bgcolor("black")

 # initializing objects to use in main function
total_score = score.Score()
tim = snake.Snake()
food_game = food.Food()

 # tim starts moving and food appear by calling method start and appear_food
tim.start()
food_game.appear_food()

 # make movements by using arrow keys
display.listen()
display.onkey(tim.go_up , "Up")
display.onkey(tim.go_down, "Down")
display.onkey(tim.go_left,"Left")
display.onkey(tim.go_right,"Right")

 # main loop of the game , it ends only if snake collides with wall or tail
game_on = True
while game_on:

     # update screen after all segments move , actually each segment move on its own by following a path so updates screen when all moves
    display.update()
    time.sleep(0.1)

     # method made in snake class to make snake move
    tim.move()

     # find a borderline for screen 600/600 and if snake exceed this range then game over
    if  tim.segments[0].xcor() > 280 or tim.segments[0].xcor()<-280 or tim.segments[0].ycor() >280 or tim.segments[0].ycor() < -280:
        game_on = False
        total_score.game_over()   #-------- game over is a method in score file

     # check collision with tail by checking distance between head(seg[0]) and other segments
    for x in tim.segments[1:]:  #---------- list slicing concept to exclude an element from list
            if tim.segments[0].distance(x)< 10:
                total_score.game_over()    #-------- game over is a method in score file
                game_on = False

     # if the distance between head(seg[0]) and food is less than 10 pixels than call appear_food method which makes
     # food appear at random x and y coordinates
     # use extend method to add new segment at last segment[3 then 4 and so on ]
     # use new_score method that increase score
    if tim.segments[0].distance(food_game) < 15:
        food_game.appear_food()
        tim.extend()
        total_score.new_score()

display.exitonclick()