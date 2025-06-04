#recursive function(call function inside a function)
#Factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1
    return n* fact(n-1)
n=int(input("Ente a number:"))
f=fact(n)
print("Factorial of ",n,"is:",f)
"""
Ente a number:2
Factorial of  2 is: 2
"""
#Fibonacci series of n numbers
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter a number:"))
for i in range(0,n):
    x=fibo(i)
    print(x)
"""
Enter a number:4
0
1
1
2
"""
