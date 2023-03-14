from turtle import Turtle, Screen
import random

ken = Turtle()
ken.shape("arrow")  # the shape of the turtle
ken.pensize(2)
ken.hideturtle()


def dashed_line():
	for i in range(10):
		ken.forward(10)
		ken.penup()
		ken.forward(10)
		ken.pendown()


def draw_shape(n):
	for i in range(n):
		ken.forward(100)
		ken.left(360 / n)


colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black", "white", "maroon",
		  "teal", "navy", "olive"]

for num in range(3, 11):
	color = random.choice(colors)
	ken.color(color)
	draw_shape(num)

screen = Screen()  # the screen, but it won't stay
screen.exitonclick()  # click on exit, it will stay but only disappear when you click the screen
