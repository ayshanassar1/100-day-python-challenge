# Day 1 - Python Basics and Data Types

# 1. Print Hello World!
print("Hello World!")
# Output: Hello World!

# 2. Take input, ask name and print it
name = input("Enter your name: ")
print("Hello, " + name + "!")
# Example Input: Bilal
# Output: Hello, Bilal!

# 3. Add, subtract, divide, multiply 2 user input numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = float(input("Enter third number: "))
add= num1 + num2
sub = num1 - num2
mult= num1 * num2
div = num1 / num2

print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mult}")
print(f"Division: {div}")
# Example Input: 
num1=10,
num2=5
num3=1.2
# Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2

# 4. Check data type
print(type(name))       # <class 'str'>
print(type(num1))       # <class 'int'>
print(type(num2))       # <class 'float'>

# 5. Take input as int, float, string and print a line
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
city = input("Enter your city: ")

print(f"You are {age} years old, {height} meters tall and live in {city}.")
# Example Input: 
age =25,
height =1.7,
city =Mumbai
# Output: You are 25 years old, 1.7 meters tall and live in Mumbai.

# 6. Boolean conversion
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False
print(bool("Hello"))    # True
print(bool([]))         # False
print(bool([1, 2, 3]))  # True

