# Comparing 3 numbers to find the largest one
num1 = 50
num2 = 265
num3 = 10
print("The numbers are: 50, 265, 10")

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")