a=list(map(int,input("Enter array elements:").split()))
n=len(a)
for i in range(n):
        for j in range((i+1),n):
            if(a[i]>a[j]):
              t=a[i]
              a[i]=a[j]
              a[j]=t
print(a)

"""
output:
Enter array elements:5 3 2 8 1 9 0 6
[0, 1, 2, 3, 5, 6, 8, 9]
"""
