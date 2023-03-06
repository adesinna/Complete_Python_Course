height = float(input('Enter your height in meter:\n'))
bill = 0

if height < 1.2:
    print("you can't ride")
else:
    print("you can ride")
    age = int(input("Enter your age:\n"))

    if age < 12:
        bill += 5
    elif 12 <= age < 18:
        bill += 7
    else:
        bill += 12

    photo = input('Do you want your photo taken, y or n:\n')

    if photo == 'y':
        bill += 3
    elif photo == 'n':
        bill += 0

print(f'Your total bill is {bill}')

