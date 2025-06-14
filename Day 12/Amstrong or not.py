n = int(input("Enter a number: "))
t = n
d = len(str(n))
s = 0

while t > 0:
    r = t % 10
    s += r ** d
    t //= 10

if s == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

"""
Case 1:
Enter a number: 153
153 is an Armstrong number

Case 2:
Enter a number: 123
123 is not an Armstrong number
"""
