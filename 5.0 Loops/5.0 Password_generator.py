import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_number = int(input('Enter number of letters(max of 10):\n'))
numbers_number = int(input('Enter number of numbers(max of 9):\n'))
numbers_symbols = int(input('Enter number of symbols(max of 6):\n'))


pass_word = []

pass_letter = random.sample(letters, letter_number)
pass_number = random.sample(numbers, numbers_number)
pass_symbol = random.sample(symbols, numbers_symbols)


pass_word.extend(pass_letter)
pass_word.extend(pass_number)
pass_word.extend(pass_symbol)

random.shuffle(pass_word)  # you can not assign random.shuffle to a variable

print("".join(pass_word))





