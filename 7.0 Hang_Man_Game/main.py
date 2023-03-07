import hangman_art
import hangman_words
import random

print(hangman_art.logo)  # get the logo

random_word = random.choice(hangman_words.word_list)
stages = hangman_art.stages
lives = 7
display = []


for i in range(len(random_word)):
    display.append("_")


end_of_game = False  # terminator


while not end_of_game:
    print(f'You have {lives} left')
    print(f"{' '.join(display)}")  # join the dashes
    guess = input('Guess a letter:\n').lower()

    if guess in random_word:
        for i in range(len(display)):
            if guess == random_word[i]:  # don't use index since it will only find it once
                display[i] = guess

    else:
        print(stages[lives - 1])
        lives -= 1

    if "_" not in display:  # end game condition
        print("You win")
        end_of_game = True

    if lives == 0:  # end game condition
        print("End of game you lose")
        print(f"The word was {random_word}")
        end_of_game = True
