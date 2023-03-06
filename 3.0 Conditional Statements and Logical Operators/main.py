# if and else statements is used for conditional statements

number = int(input('Enter number:\n'))

if number > 0:
    print('It is positive')
else:
    print("It is negative")

# if the condition is more than two conditions, use elif

num = int(input('Enter number:\n'))

if num > 0:
    print('It is positive')
elif num == 0:
    print("It is neither negative nor positive")
else:
    print("It is negative")


# Logical Operators
# and, or, not
# and # both conditions must be true
# or # one of the condition must be true
# not # this will reverse it boolean of the statement
