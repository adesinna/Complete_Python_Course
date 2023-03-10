import random
from game_data import data
from arts import logo, vs

print(logo)


def name():
	celeb = random.choice(data)
	return celeb


def game():
	score = 0
	end = False
	celeb_a = name()
	while not end:
		celeb_b = name()
		if celeb_a == celeb_b:
			game()  # restart game

		print(f"Compare {celeb_a['name']}, {celeb_a['description']}, from {celeb_a['country']}")
		print(vs)
		print(f"Compare {celeb_b['name']}, {celeb_b['description']}, from {celeb_b['country']}")

		answer = input("Who has more followers A or B:\n").lower()

		if answer == 'a' and (celeb_a['follower_count'] > celeb_b['follower_count']):
			score += 1

		elif answer == 'b' and (celeb_a['follower_count'] < celeb_b['follower_count']):
			score += 1
			celeb_a = celeb_b

		else:
			print(f"A has {celeb_a['follower_count']} ")
			print(f"B has {celeb_b['follower_count']}")
			print(f"{score}")
			print("Game Over")
			end = True

		print(f"Your score is {score}")


game()






