n = int(input("Enter a number: "))
s = 0
t = n

while t > 0:
    s += t % 10
    t //= 10

if n % s == 0:
    print(n, "is a Harshad number")
else:
    print(n, "is not a Harshad number")

"""
Case 1:
Enter a number: 18
18 is a Harshad number

Case 2:
Enter a number: 19
19 is not a Harshad number
"""
