from turtle import Turtle


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color('white')
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear() # clear the last score
		self.goto(-100, 200)  # place here for left
		self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
		self.goto(100, 200)  # place here for right
		self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

	def l_point(self):
		self.l_score += 1
		self.update_scoreboard()

	def r_point(self):
		self.r_score += 1
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)  # place here for right
		self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))

