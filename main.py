import time
import os
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

token = os.environ.get("AZURE_SECRET_TOKEN")
screen = Screen()
screen.setup(720, 720)
screen.bgcolor("black")
screen.title("Rắn săn mồi ok ?")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segment[0].xcor() >= 360 or snake.segment[0].xcor() <= -360 or snake.segment[0].ycor() >= 360 or snake.segment[0].ycor() <= -360:
        game_is_on = False
        scoreboard.game_over()

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    if(snake.bite_tail()):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
