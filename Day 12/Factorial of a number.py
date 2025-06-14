n = int(input("Enter a number: "))
f = 1

for i in range(1, n + 1):
    f *= i

print("Factorial of", n, "is", f)

"""
Case 1:
Enter a number: 5
Factorial of 5 is 120

Case 2:
Enter a number: 0
Factorial of 0 is 1
"""
