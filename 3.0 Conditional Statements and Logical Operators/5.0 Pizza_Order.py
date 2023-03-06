bill = 0
pizza_type = input('Enter Pizza\n'
                   'L for Large\n'
                   'M for Medium\n'
                   'S for Small\n'
                   ':')
pepperoni = input('Do you want pepperoni\n'
                  'Yes or No:\n')

extra_cheese = input('Do you want extra cheese\n'
                     'Yes or No:\n')

if pizza_type.lower() == 'l':
    bill += 25

    if pepperoni.lower() == 'yes':
        bill += 3

    if extra_cheese.lower() == 'yes':
        bill += 1

elif pizza_type.lower() == 'm':
    bill += 20

    if pepperoni.lower() == 'yes':
        bill += 3

    if extra_cheese.lower() == 'yes':
        bill += 1

elif pizza_type.lower() == 's':
    bill += 15

    if pepperoni.lower() == 'yes':
        bill += 2

    if extra_cheese.lower() == 'yes':
        bill += 1

print(f"The total bill is ${bill}")