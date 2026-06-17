# Basic Calculator Program
# Function to add two numbers
# Function to subtract two numbers
# Function to multiply two numbers
# Function to divide two numbers
# Run the calculator repeatedly until the user exits
# Display calculator menu options
# Get the user's choice
# Get the first number from the user
# Get the second number from the user
# Perform addition
# Perform subtraction
# Perform multiplication
# Perform division
# Check if the divisor is not zero
# Display error message for division by zero
# Handle invalid menu choices
# Ask the user if they want to perform another calculation
# Exit the calculator if the user does not enter 'yes'

#Basic Calculator
while True:
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    print("Select operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division" )
    choice = input("Enter choice(1/2/3/4):")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print("Result: ", add(num1,num2))
    elif choice == '2':
        print("Result: ", subtract(num1,num2))
    elif choice == '3':
        print("Result: ", multiply(num1,num2))         
    elif choice == '4':
        if num2 != 0:
            print("Result: ", divide(num1,num2))
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Exiting the calculator. Goodbye!")
        break