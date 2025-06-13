a = list(map(int, input("Enter numbers to sort: ").split()))
n = len(a)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    # Swap the found minimum with current position
    a[i], a[min_index] = a[min_index], a[i]
print("Sorted list:", a)
"""
output:
Enter numbers to sort: 3 2 1 4 5 6
Sorted list: [1, 2, 3, 4, 5, 6]
"""
