import art
import random

# black jack rules
#  dealer gives you to card

print(art.logo)
print('Welcome to Black Jack')
cards_dict = {
	'ace': 11,
	'king': 10,
	'queen': 10,
	'jack': 10,
	'ten': 10,
	'nine': 9,
	'eight': 8,
	'seven': 7,
	'six': 6,
	'five': 5,
	'four': 4,
	'three': 3,
	'two': 2
}

card_choices = []

for key, value in cards_dict.items():
	card_choices.append(key)


player = input('Enter your name:\n')


def deal():
	card = random.choice(card_choices)
	return card


def score(list_card):
	total = 0
	for item in list_card:
		total += cards_dict[item]
	if ('ace' in list_card) and total > 21:
		total -= 10

	return total


end = False
computer_card = []
player_card = []

computer_card.append(deal())

player_card.append(deal())
player_card.append(deal())


print(f"{player}'s cards are {player_card}")
print(f'computer card is {computer_card}')

while not end:
	hit = input('Do you want to deal? "yes" or "no":\n')

	if hit == "yes":
		player_card.append(deal())
		computer_card.append(deal())

		score_computer = score(computer_card)
		score_player = score(player_card)

		print(f"{player}'s cards are {player_card} with score {score_player}")
		print(f"computer cards are {computer_card} with score {score_computer}")

		if score_player > 21:
			print(f"{player} lose")
			break  # if you use end=True here, it will still check other conditions but break do not give a shit.!

		if score_computer < 17:
			print("Dealer card is less than 17")
			computer_card.append(deal())
			score_computer = score(computer_card)
			print(f"computer cards are {computer_card} with score {score_computer}")
			print(f"{player}'s cards are {player_card} with score {score_player}")

		if score_computer > 21:
			print(f'{player} win')
			break

		if score_computer == score_player:
			print('It is a draw')
			end = True

		if score_player < score_computer <= 21:
			print(f"{player} lose")
			end = True
		if score_computer < score_player <= 21:
			print(f"{player} win")
			end = True

	else:
		print(f"Good Bye {player}")
		end = True










