from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # the background color
screen.title("Snakey")
screen.tracer(0)  # so the segments do not chase each other

snake = Snake()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_on = True
while game_on:
	screen.update()  # update when the for loop is done
	time.sleep(0.1)  # interval of update

	snake.move()


screen.exitonclick()
