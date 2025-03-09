# Prompt user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# input numbers are
num1 = 5
num2 = 0

# Ask the user to choose an operation
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

# Perform the selected operation
if operation == "add":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "divide":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation. Please choose add, subtract, multiply, or divide.")
