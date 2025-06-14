"""
n = 3
Output:
  * 
 * * 
* * * 
 * * 
  * 
"""
n = int(input("Enter number of rows: "))
# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
