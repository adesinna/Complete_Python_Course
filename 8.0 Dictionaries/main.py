# Dictionaries in python are used to store data with key or name

dict_1 = {
    'name': 'Aladesae Adesina',
    'places': ['Ibadan', 'Lagos', 'Port-Harcourt'],
    'work': {'role': "devops", 'experience': 2, }

}

print(dict_1['name'])

# You can use the dict function

dict_2 = dict(name='Adesina', level=2, work=['Devops', 'ML', "Python"], dict_3={'state': 'Ibadan','origin': 'Ondo'})

print(dict_2)

# looping through a dictionary

for (key, value) in dict_1.items():
    print(key)
    print(value)

