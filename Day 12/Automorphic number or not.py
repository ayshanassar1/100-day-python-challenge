n = int(input("Enter a number: "))
s = n ** 2

if str(s).endswith(str(n)):
    print(n, "is an Automorphic number")
else:
    print(n, "is not an Automorphic number")

"""
Case 1:
Enter a number: 76
76 is an Automorphic number

Case 2:
Enter a number: 25
25 is not an Automorphic number
"""
