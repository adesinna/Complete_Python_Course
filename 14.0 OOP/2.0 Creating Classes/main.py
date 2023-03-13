# How to create classes of your own

class User:
	def __init__(self):  # attributes must be strings
		print('hello')


user_1 = User()  # this is how to create an object

print(type(user_1))
user_1.id = '001'
user_1.username = 'adesina'

print(user_1.username)

