def calculator():
    try:
        num1 = float(input("10: "))
        num2 = float(input("5: "))
        operation = input("+ (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values...")

# Run the calculator
calculator()