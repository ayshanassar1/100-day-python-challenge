a=list(map(int,input("Enter array elements:").split()))
n=len(a)
x=int(input("Enter the element to search:"))
f= False
for i in range(n):
    if(a[i]==x):
        f=True
        print("Number found")
        break
if not f:
    print("Number not found")
  """
  case 1:
Enter array elements:1 3 6 8 9
Enter the element to search:9
Number found
case 2:
Enter array elements:1 2 3
Enter the element to search:4
Number not found
"""
