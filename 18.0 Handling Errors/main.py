# There will always be errors in your code, but you can handle it.

# FileNotFound means the file is not there
# Key error means the key don't exist in a dictionary
# Index error the index don't exist in the list
# Type error means that type of data can't perform the operation


# Use TEEF, to handle error Try, Except, Else, Finally

# Try: Something that might cause the error
# Except: Do this if the error occurs
# Else: Do this if the error didn't happen
# Finally: Do this whether it is Except or Else that worked


# FileNotFound
try:
	file = open('file.txt')
# try and open it
	# a_dictionary = {'key':'value'}
	# print(a_dictionary['shina']) # I expect a key error

# You can have multiple except for different errors

except FileNotFoundError:  # you must give it the specific error
	open('file.txt', 'w')  # create it from scratch

# except KeyError as message:
# 	print(message)

else:  # it would do this if there is no exceptions/error
	content = file.read()
	print(content)

finally:  # do this no matter what happens, it is not often used
	file.close()
	print('Bye')









