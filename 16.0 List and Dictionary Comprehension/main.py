# List comprehension
# new_list = [ do_this for item in list if condition is true]
import random

numbers = list(range(20))

new_list = [(i+1) for i in numbers]  # helps you do it on the same line
print(new_list)

list_2 = [i for i in numbers if i % 2 == 0]  # the list is like appending i
print(list_2)


# Dictionary comprehension

# new_dict = { new_key:new_value for (key,value) in dict.items() if condition is true}


dict1 = {
	'Name': 'Adesina'
}

dict2 = {key: value.upper() for key, value in dict1.items()}

print(dict2)

numbers_3 = [str(i) for i in numbers]

dict_3 = {str_num: random.randint(1, 10) for str_num in numbers_3 }
print(dict_3)
