n = int(input("Enter a number: "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")

"""
Case 1:
Enter a number: 6
6 is a Perfect Number

Case 2:
Enter a number: 10
10 is not a Perfect Number
"""
