# Raising Errors

age = input("Enter your age: ")

try:
	n = int(age)

except ValueError as message:  # go get the message too
	print('Bad Integer')   # do this if you get ValueError
	print(f'Error is: {message}') # do this too

else:
	if 0 < n < 100:
		print(n * 2)
	else:
		raise ValueError('age is above 100')  # your special error

finally:
	print('good bye')









