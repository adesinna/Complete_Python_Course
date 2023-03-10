import random

rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choices)
user_name = input('Enter user name:\n')
user_choice = input('Enter \nr for rock\np for paper\ns for scissors\n:')

if user_choice.lower() == 'r':
    print(rock_img)
    print('vs')

    if computer_choice == 'rock':
        print(rock_img)
        print('This is a tie')

    elif computer_choice == 'paper':
        print(paper_img)
        print('Computer Wins')

    else:
        print(scissors_img)
        print(f"{user_name} wins")

elif user_choice.lower() == 'p':
    print(paper_img)
    print('vs')

    if computer_choice == 'rock':
        print(rock_img)
        print(f"{user_name} wins")

    elif computer_choice == 'paper':
        print(paper_img)
        print('This is a tie')

    else:
        print(scissors_img)
        print('Computer Wins')

else:
    print(scissors_img)
    print('vs')

    if computer_choice == 'rock':
        print(rock_img)
        print('Computer Wins')

    elif computer_choice == 'paper':
        print(paper_img)
        print(f"{user_name} wins")

    else:
        print(scissors_img)
        print('This is a tie')
