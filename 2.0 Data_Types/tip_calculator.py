total_bill = float(input("Enter total amount in $:\n"))
num_of_persons = int(input('Enter the number of people:\n'))
tip_percentage = int(input("Enter the tip percentage:\n"))
tip_per_person = (total_bill/num_of_persons) * (tip_percentage/100)

answer = round(tip_per_person, 2)

print(f'Each person is to pay ${answer}')
