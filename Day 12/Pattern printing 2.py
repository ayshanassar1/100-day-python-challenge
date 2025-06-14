"""
Number of rows=3

	             *
          *    *    *
     *       *       *     *  
"""
n=int(input("how much rows are required:"))
j=1
for i in range(1,n+1,2):
    print(" "* (n-i) ,"* "*j)
    j=j+2
print("* "*j)
