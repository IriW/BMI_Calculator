print("Welcome to BMI calculator.")
weight=float(input("Enter your weight in kg:\n"))
height=float(input("Enter your height in m:\n"))
BMI=round(weight/height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >=30:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")