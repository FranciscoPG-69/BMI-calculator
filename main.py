# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = float(height)
b = int(weight)

BMI = float(b / (a ** 2))
print(BMI)