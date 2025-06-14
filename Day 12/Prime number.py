n = int(input("Enter a number: "))
f = 0

if n <= 1:
    print(n, "is not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            f = 1
            break
    if f == 0:
        print(n, "is a Prime Number")
    else:
        print(n, "is not a Prime Number")

"""
Case 1:
Enter a number: 7
7 is a Prime Number

Case 2:
Enter a number: 12
12 is not a Prime Number
"""
