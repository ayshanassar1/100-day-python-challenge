a = list(map(int, input("Enter array elements: ").split()))
a.sort()
print("Sorted array:", a)
x = int(input("Enter the element to search: "))
low = 0
high = len(a) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        print("Number found ")
        found = True
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Number not found")
"""
case 1:
Enter array elements: 2 3 1 5 7 6 9 8
Sorted array: [1, 2, 3, 5, 6, 7, 8, 9]
Enter the element to search: 6
Number found
case 2:
Enter array elements: 6 1 2 4 3
Sorted array: [1, 2, 3, 4, 6]
Enter the element to search: 5
Number not found
"""
