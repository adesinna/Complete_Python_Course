import random

num_1 = random.randint(1, 10)  # gives a random integer n in [a,b] any you run it

print(num_1)

num_2 = random.random() # gives a random float between [0, 1)

print(num_2)

# List is used to store data
# List can be represented by []

list_1 = ['adesina', 3.48, -8, True]

list_2 = list(range(100))  # 0 - 99
print(list_2)

# Indexing
# list_name[index] will produce the item at that index
# if there is the index is greater than the len(list_name) - 1, then go get index error

# Slicing
# list_name[start: end: step] # not that the end will not be included

# You can convert a string into a list

str_1 = "h l o"
list_3 = str_1.split(" ")
print(list_3)

# You can nest list inside a list

list_4 = [list_1, list_3]

print(list_4)


