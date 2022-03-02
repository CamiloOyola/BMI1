print("Write your weight and height")
weight = float(input("Weight[kg]:"))
height = float(input("Height[m]:"))
BMI = (weight / height ** 2)
print("Your BMI is:" + str(BMI))

if BMI < 16:
    print("Your nutritional status is serious")
elif 18.6 <= BMI < 20:
    print("Your weight is insufficient")
elif 20 <= BMI < 26.5:
    print("Your wight is normal")
elif 26.5 <= BMI < 30:
    print(" You are overweight")
elif BMI >= 30:
    print(" You are obesity")
print("*"*35)
