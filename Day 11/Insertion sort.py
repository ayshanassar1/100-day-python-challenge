a = list(map(int, input("Enter numbers to sort: ").split()))

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print("Sorted list:", a)
"""
output:
Enter numbers to sort: 4 5 1 7 2 0 3 9
Sorted list: [0, 1, 2, 3, 4, 5, 7, 9]
"""
