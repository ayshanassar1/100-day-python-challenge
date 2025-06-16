def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "❌ Cannot divide by zero"

def calculator():
    print("🧮 Simple Calculator")
    print("Select operation:")
    print("1. ➕ Add")
    print("2. ➖ Subtract")
    print("3. ✖️ Multiply")
    print("4. ➗ Divide")

    try:
        choice = input("Enter choice (1-4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("❌ Invalid input. Please choose between 1 and 4.")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

# Run the calculator
calculator()
"""
Output:
🧮 Simple Calculator
Select operation:
1. ➕ Add
2. ➖ Subtract
3. ✖️ Multiply
4. ➗ Divide
Enter choice (1-4): 1
Enter first number: 10
Enter second number: 20
Result: 30.0
"""
