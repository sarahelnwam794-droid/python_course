def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("--- Smart Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    result = add(num1, num2)
    print(f"\nResult: {result}")
elif choice == "2":
    result = subtract(num1, num2)
    print(f"\nResult: {result}")
else:
    print("\nInvalid choice! Please select 1 or 2.")