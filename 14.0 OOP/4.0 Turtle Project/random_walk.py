import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255) # to allow us to use rgb mode


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color_tuple = (r, g, b)
	return color_tuple


num_steps = 500
step_size = 20
ken = Turtle()
ken.shape("turtle")  # the shape of the turtle
ken.pensize(10)
ken.speed('fastest')


for i in range(num_steps):
	ken.color(random_color())
	angle = random.randint(0, 360)
	ken.right(angle)
	ken.forward(step_size)


screen = Screen()  # the screen, but it won't stay
screen.exitonclick()  # click on exit, it will stay but only disappear when you click the screen
