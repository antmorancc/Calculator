def calculator():
    print("Welcome to the Calculator Program!")
    print("Available operations: +, -, *, /")
    
    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Input operation
    operation = input("Choose an operation (+, -, *, /): ")
    
    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result is: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result is: {result}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    else:
        print("Invalid operation! Please choose from +, -, *, /.")
    
    print("Thank you for using the Calculator!")

# Run the program
if __name__ == "__main__":
    calculator()
