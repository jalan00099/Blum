def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """The main function to run the calculator"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Enter 'q' to quit.")

    while True:
        # Take input from the user
        choice = input("\nEnter choice(1/2/3/4/q): ")

        # Check if the user wants to quit
        if choice.lower() == 'q':
            print("Thank you for using the calculator!")
            break

        # Check if the choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input. Please enter a valid choice.")

# Run the calculator
if __name__ == "__main__":
    calculator()
