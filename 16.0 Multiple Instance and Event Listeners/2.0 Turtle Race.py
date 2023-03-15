from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)  # the dimension of the screen
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50 , 89]
turtles = []

for i in range(len(colors)):
	new_turtle = Turtle(shape='turtle')
	new_turtle.color(colors[i])
	new_turtle.penup()
	new_turtle.goto(x=-240, y=y_position[i])
	turtles.append(new_turtle)


race = False

if user_bet:   # to make sure input is on before the race
	race = True

while race:

	for tur in turtles:
		if tur.xcor() > 230:  # when to end race
			race = False
			winning_color = tur.pencolor()

			if winning_color == user_bet:
				print(f'You won, winning color is {winning_color}')
			else:
				print(f'You lose, winning color is {winning_color}')

		rand_distance = random.randint(1, 10)
		tur.forward(rand_distance)


screen.exitonclick()