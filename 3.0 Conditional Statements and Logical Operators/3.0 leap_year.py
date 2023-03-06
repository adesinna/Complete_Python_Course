# A leap must be divisible by 4
# Must not divide 100
# If it divides 100, it must also divide 400

year = int(input("Enter year: \n"))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print(f'{year} is a leap year')
    elif year % 100 != 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is a not leap year')
else:
    print(f'{year} is a not leap year')

