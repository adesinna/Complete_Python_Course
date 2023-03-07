numbers = input('Enter numbers:\n').split(' ')  # this will come in as string

numbers_floats = []

for num in numbers:
    numbers_floats.append(float(num))

print(numbers_floats)

lowest = numbers_floats[0]

for num in numbers_floats:
    if num < lowest:
        lowest = num

print(f"The lowest value is {lowest}")

