from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(n=0)
screen.listen()
snake=Snake()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
food = Food()
scoreboard=ScoreBoard(screen)


is_on=True
while is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()
    if snake.head.distance(food)<15: #collision with the food
        food.refresh()
        scoreboard.increase()
        snake.extend_snake()

    if (snake.head.xcor()>280 # collision with the wall
            or snake.head.xcor()<-280
            or snake.head.ycor()>280
            or snake.head.ycor()<-280):
        scoreboard.reset_score()
        snake.reset()




    for segments in snake.segments[1:]:#collision with the tail
        if snake.head.distance(segments)<10:
            scoreboard.reset_score()
            is_on=False






































screen.exitonclick()