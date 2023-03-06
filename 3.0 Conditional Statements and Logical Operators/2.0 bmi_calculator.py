# BMI = weight / (height*height)

height = float(input("Enter your height in meter:\n"))
weight = float(input("Enter your weight in kg:\n"))

bmi = weight / (height ** 2)

bmi = round(bmi, 2)

if bmi <= 18.5:
    print(f'Your bmi is {bmi} and you are underweight ')

elif 18.5 < bmi <= 25:
    print(f'Your bmi is {bmi} and you are normal weight ')

elif 25 < bmi <= 30:
    print(f'Your bmi is {bmi} and you are overweight ')
elif 30 < bmi <= 35:
    print(f'Your bmi is {bmi} and you are obese ')
else:
    print(f'Your bmi is {bmi} and you are clinically obese ')

