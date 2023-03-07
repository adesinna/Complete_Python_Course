numbers = input('Enter numbers:\n').split(' ')  # this will come in as string

numbers_floats = []

for num in numbers:
    numbers_floats.append(float(num))

print(numbers_floats)

highest = numbers_floats[0]

for num in numbers_floats:
    if num > highest:
        highest = num

print(f"The highest value is {highest}")

