#simple for loop

n=int(input("Enter a limit:"))
for i in range(1,(n+1)):
    print(i)
"""output:
Enter a limit:5
1
2
3
4
5
"""

#Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
"""
output:
apple
banana
cherry
"""

#Simple while loop
n=int(input("Enter a limit:"))
i=1
while i <= n:
    print(i)
    i=i+1
"""
output:
Enter a limit:5
1
2
3
4
5
"""

#breaking the loop using break
n=int(input("Enter a limit:"))
for i in range(1,n):
    if i == 5:
        break
    print(i)
"""
output
Enter a limit:20
1
2
3
4
"""

#skip a step using continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
"""
output:
1
2
4
5
"""
