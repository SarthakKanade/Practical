def calculator():
    print("Welcome to the Python Calculator!")
    print("Select the operation you'd like to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        try:
            # Get user choice
            choice = input("\nEnter the number corresponding to your choice: ")
            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid input. Please choose a valid option.")
                continue

            # Get user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the operation
            if choice == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()

print("done changes")
