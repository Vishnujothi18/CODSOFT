def calculator():
    print("Simple Calculator")
    
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for an operation
    print("\nSelect the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("\nEnter your choice (1/2/3/4): ")
    
    # Perform the calculation based on user choice
    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 != 0:  # Handle division by zero
            result = num1 / num2
            operation = "/"
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid input. Please enter a valid operation.")
        return
    
    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
