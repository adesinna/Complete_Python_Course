# Scopes in Python
# Name space only affect name functions but does affect if,while or for.

count = 1

if 3 < 4:
	count += 1

print(count)


#
# def counter():
# 	count += 1 # This line will error out, it can't access the global scope, you cannot manipulate them inside a function
# 	return count   # it can return a global variable scope

# to tackle this we use global


def counter():
	global count  # to make function to recognise them

	count += 1  # Now you can manipulate them, but it is not good practice

	print(count)


counter()

# When you define a constant, global scope

PI = 3.14


def area(r):
	a = PI * r * r  # You can use them, but cannot munipulate them
	return a


y = area(8)
print(y)

