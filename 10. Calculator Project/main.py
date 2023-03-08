import arts


def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	return a / b


def power(a, b):
	return a ** b


symbol_dict = {  # dictionaries can store just the function without the brackets
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
	'**': power,

}

print(arts.logo)


def calc():
	end = False

	first = float(input('Enter num:\n'))

	while not end:
		for key, value in symbol_dict.items():  # key,value to use items
			print(key)

		operation = input('Enter operation:\n')
		second = float(input('Enter num:\n'))

		result = symbol_dict[operation](first, second)

		print(result)

		con = input('Do you want to continue? "yes" or "no":\n').lower()

		if con == 'no':
			end = True

		else:
			first = result

	quit_calc = input('Do you want to quit calculator? "yes" or "no":\n').lower()

	if quit_calc == 'no':
		calc()  # recursion
	else:
		print('Good Bye')


calc()  # not assigned because no return, print was used instead
