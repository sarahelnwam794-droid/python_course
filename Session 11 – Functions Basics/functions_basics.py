def say_hello():
    print("Welcome to Python Functions!")

say_hello()

def greet_student(name):
    print(f"Hello, {name}! Great job today.")
greet_student("Ahmed")
greet_student("Sara")

def add_numbers(a, b):
    return a + b 

result = add_numbers(5, 10)
print(f"The sum result is: {result}")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

print("--- My Calculator Function ---")

print("Addition Result:", add(20, 10))



print("Subtraction Result:", subtract(20, 10))