#call simple function
def f():
    print("July")
print("Start")
f()
print("End")
 
"""
Start
July
End
"""

#call function with return value
def add(a,b):
    s=a+b
    return s
a=int(input("Enter a:"))
b=int(input("Enter b:"))
s=add(a,b)
print("Sum:",s)
"""
Enter a:2
Enter b:3
Sum: 5
"""
