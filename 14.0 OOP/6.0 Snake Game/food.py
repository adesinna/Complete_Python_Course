from turtle import Turtle
import random


class Food(Turtle):  # class inheritance, note you can inherit from more than one class

	def __init__(self):
		super().__init__()  # initialize the class
		self.shape('circle')
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # go make it a small circle
		self.color("blue")
		self.speed('fastest')
		self.reset_food()

	def reset_food(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)

	def dummy(self):
		super().speed()  # this is how to use the inheritance method
