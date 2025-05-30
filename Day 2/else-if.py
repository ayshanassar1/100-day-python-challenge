# simple else-if statement

t=int(input("Enter temperature:"))
if (t>30):
  print("Temperature is hot")
else:
  print("Temperature is cold")
"""
output:
Enter temperature:36
Temperature is hot
"""

#if-elif-else statement
x=int(input("Enter a number:"))
if(x>0):
  print("Number is positive")
elif(x<0):
  print("Number is Negative")
else:
  print("Number is zero")
"""
output
Enter a number:3
Number is positive
"""
#nested if statement 
n=int(input("Enter a Number:"))
if(n>0):
  if(n%2==0):
    print("number is positive and prime")
  else:
    print("number is positive and not prime")
else:
  print("number is zero or negative")
"""
output:
Enter a Number:6
number is positive and prime
"""

#check multiple condition with AND
age = int(input("Enter age:"))
has_license = True
if age >= 18 and has_license:
    print("Allowed to drive")
else:
    print("Not allowed to drive")
"""
output:
Enter age:20
Allowed to drive
"""

#check condition inside a function:
def check_temperature(temp):
    if temp > 30:
        return "It's hot"
    elif temp < 10:
        return "It's cold"
    else:
        return "It's moderate"
print(check_temperature(25))
"""
output:
It's moderate
"""

#ternary operator
age = int(input("Enter age:")
status = "Adult" if age >= 18 else "Minor"
print(status)
"""
output:
Adult
"""

