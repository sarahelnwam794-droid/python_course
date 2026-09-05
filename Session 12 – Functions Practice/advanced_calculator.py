def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero."
    return a % b

history = []

print("--- Welcome to the Advanced Mini Calculator ---")
username = input("Please enter your name: ")
print(f"Hello, {username}! Let's do some math.\n")

print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Power (**)")
print("6. Modulus (%)")
print("7. View History ")
print("Type 'q' at any time to exit.")

while True:
    choice = input(f"\n{username}, choose an option (1-7) or 'q' to quit: ")
    
    if choice.lower() == 'q':
        print(f"Thank you for using the calculator, {username}. Goodbye!")
        break
        
    if choice == '7':
        if not history:
            print("No history yet!")
        else:
            print("\n--- Calculation History ---")
            for record in history:
                print(record)
            print("---------------------------")
        continue
        
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers, not letters!")
            continue
            
        if choice == "1":
            result = add(num1, num2)
            op_symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op_symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op_symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op_symbol = "/"
        elif choice == "5":
            result = power(num1, num2)
            op_symbol = "**"
        elif choice == "6":
            result = modulus(num1, num2)
            op_symbol = "%"
            
        print(f"Result: {result}")
        
        if "Error" not in str(result):
            history.append(f"{num1} {op_symbol} {num2} = {result}")
            
    else:
        print("Invalid choice, please try again!")