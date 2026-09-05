def say_hello():
    print("welcome to python functions")

say_hello()

def great_student(name):
    print(f"hello {name}")

great_student("mamdouh")
great_student("ratal")

def add_numbers(a, b):
    return a + b

result = add_numbers(1, 2)
print(f"result is {result}")

def subtract_numbers(a, b):
    return a - b

print("my calculator functions")
print(add_numbers(1, 2))
print(subtract_numbers(a=1, b=2))