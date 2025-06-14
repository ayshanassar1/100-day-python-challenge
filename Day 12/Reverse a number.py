n = int(input("Enter a number: "))
r = 0

while n > 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10

print("Reversed number is:", r)

"""
Case 1:
Enter a number: 1234
Reversed number is: 4321
"""
