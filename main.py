import time
import turtle
import snake
import food
display = turtle.Screen()
display.tracer(0)
display.setup(width=600, height=600)
display.title("THE SNAKE GAME")
display.bgcolor("black")

tim = snake.Snake()
tim.start()
food_game = food.Food()
food_game.appear_food()

display.listen()
display.onkey(tim.go_up , "Up")
display.onkey(tim.go_down, "Down")
display.onkey(tim.go_left,"Left")
display.onkey(tim.go_right,"Right")

game_on = True

while game_on:
    display.update()
    delay = time.sleep(0.1)
    tim.move()
    if (tim.segments[0].xcor() and tim.segments[0].ycor() ==
            food_game.food_xcor and food_game.food_ycor):
        food.appear_food()












display.exitonclick()