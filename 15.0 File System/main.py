with open('main.txt', mode='r') as file: # this how to open file in py
	context = file.read()  # must set a variable for reading
	print(context)

with open('main.txt', 'a') as file:
	file.write("\nI am a King")