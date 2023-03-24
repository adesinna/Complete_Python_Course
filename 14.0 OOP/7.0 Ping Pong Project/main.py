from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)  # will make the screen blank, turn off the animation and for it to appear back use the update method

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=paddle_r.go_up, key="Up")
screen.onkey(fun=paddle_r.go_down, key="Down")
screen.onkey(fun=paddle_l.go_up, key="w")
screen.onkey(fun=paddle_l.go_down, key='s')

game_on = True

while game_on:
	time.sleep(ball.move_speed)  # slow down by a factor of 0.1
	screen.update()  # start the animation
	ball.move()  # move the ball

	# detect collision with the wall
	if ball.ycor() > 280 or ball.ycor() < -280:  # it has hit the either walls
		ball.bounce_y()

	# detect if the ball collides with the paddle
	if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
		ball.bounce_x()

	# detect when right paddle misses and add a point to left
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_point()

	# detect when left paddle misses and add a point to right
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_point()

	# End game
	if scoreboard.r_score > 10 or scoreboard.l_score > 10:
		game_on = False
		scoreboard.game_over()

screen.exitonclick()
