height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_height = float(height)
bmi_weight = int(weight)
bmi_result = int(bmi_weight) / float(bmi_height**2) 
bmi_result =  round(bmi_result)
if bmi_result <= 18.5:
    print(f"Your BMI is{bmi_result} you are underweight.")
elif bmi_result <= 25:
    print(f"Your BMI is {bmi_result}, you have a normal weight.")
elif bmi_result <= 30:
    print(f"Your BMI is {bmi_result}, you are slightly overweight.")
elif bmi_result <= 35:
    print(f"Your BMI is {bmi_result}, you are obese.")
else:
    print( f"Your BMI is {bmi_result}, you are clinically obese.")
