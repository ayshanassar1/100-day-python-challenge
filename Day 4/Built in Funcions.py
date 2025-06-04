#built in functions
h=input("Enter sentence:") #take user input
a=int(input("Enter n:")) #take user input as integer type
print("Sentence:",h)  #provide output on the screen
print("Number:",a)
print("length:",len(h)) #print length of the line
print("Type:",type(h))
"""
Enter sentence:hello world
Enter n:3
Sentence: hello world
Number: 3
length: 11
Type: <class 'str'>
"""

#built in library function
"""
Python includes several standard libraries that offer ready-to-use functions to perform common tasks. These functions improve productivity and make code more efficient. Some commonly used functions include:

math.sqrt(x) – Returns the square root of x.
(Requires import math)

random.randint(a, b) – Returns a random integer between a and b (inclusive).
(Requires import random)

datetime.now() – Returns the current date and time as a datetime object.
(Requires from datetime import datetime)

statistics.mean(data) – Returns the mean (average) of a list of numbers.
(Requires import statistics)

os.getcwd() – Returns the current working directory of the script.
(Requires import os)

sys.exit() – Exits from Python and optionally passes a status code.
(Requires import sys)

"""
import math
n=float(input("Enter number:"))
s=math.sqrt(n) #Find square root of a number
print("Square root:",s)
"""
Enter number:4
Square root: 2.0
"""

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
