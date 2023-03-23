from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color('white')
		self.penup()
		self.goto(0, 270)
		self.update_scoreboard()
		self.hideturtle()  # the turtle of score board

	def update_scoreboard(self):
		self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # the scoreboard

	def increase_score(self):
		self.score += 1
		self.clear()  # so scores do not overlap
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)  # write it at the center
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)
