from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # the background color
screen.title("Snakey")
screen.tracer(0)  # so the segments do not chase each other

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

	# Check if snake collides with the food

	if snake.head.distance(food) < 15:  # 15px is actually the optimal for this scenario
		food.reset_food()
		snake.extend_snake()
		scoreboard.increase_score()

	# check whether snake touch the wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		game_on = False
		scoreboard.game_over()

	# if snake collides with its body

	for segment in snake.segments[1:]:  # remove the head from the list
		if snake.head.distance(segment) < 10:
			game_on = False
			scoreboard.game_over()




screen.exitonclick()
