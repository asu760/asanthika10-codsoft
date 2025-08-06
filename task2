def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations available: +  -  *  /")

    # Get user input
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operation.")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
