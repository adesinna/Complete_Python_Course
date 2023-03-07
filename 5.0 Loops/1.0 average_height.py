heights = input('Enter heights:\n').split(' ')  # this will come in as string

heights_floats = []
count = 0
sum = 0
for num in heights:
    heights_floats.append(float(num))

for num in heights_floats:
    sum += num
    count += 1

average = round((sum/count), 2)

print(f"The average height is {average}cm ")






