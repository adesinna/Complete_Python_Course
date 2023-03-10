# BMI = weight / (height*height)

height = float(input("Enter your height in meter:\n"))
weight = float(input("Enter your weight in kg:\n"))

bmi = weight / (height ** 2)

answer = round(bmi, 2)

print(f"Your bmi is {answer}")



