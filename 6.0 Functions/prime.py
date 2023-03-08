def prime(number):

    count = 0
    if number <= 1:
        return False
    else:
        for num in list(range(1, number)):
            if number % num == 0:
                count += 1

    if count == 1:
        return True
    else:
        return False


x = prime(363737091)
print(x)

