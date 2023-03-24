from turtle import Turtle


class Paddle(Turtle):

	def __init__(self, position: tuple):
		super().__init__()
		self.position = position
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)  # 20px*5 : 20px*1 since 1 turtle square is 20px*20px
		self.penup()
		self.goto(position)

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)


