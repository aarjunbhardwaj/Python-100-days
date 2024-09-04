from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jai Shree Shyam ji")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
game_over = False

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300:
        game_over = True

    if game_over:
        game_is_on = False

screen.exitonclick()
