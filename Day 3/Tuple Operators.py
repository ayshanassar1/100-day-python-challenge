#TUPLE CREATION PART
# 1. Tuple from space-separated strings
s = input("Enter string elements: ")
#Enter string elements: hello hi how are you
s1 = tuple(s.split())
print("String Tuple:", s1)
"""
Enter string elements: hello hi how are you
String Tuple: ('hello', 'hi', 'how', 'are', 'you')
"""
# 2. Tuple from space-separated integers
s = input("Enter integers: ")
s1 = tuple(map(int, s.split()))
print("Integer Tuple:", s1)
"""Enter integers: 1 2 3 4 5
Integer Tuple: (1, 2, 3, 4, 5)
"""
# 3. Mixed type tuple using eval
s = eval(input("Enter mixed elements:"))
s1 = tuple(s)
print("Mixed Tuple:", s1)
"""
Enter mixed elements:1,'hello',3,'hi'
Mixed Tuple: (1, 'hello', 3, 'hi')
"""
# 4. Tuple from loop input
n = int(input("Size of tuple"))
a= []
for i in range(n):
    v= input(f"Enter element {i+1}: ")
    a.append(v)
s = tuple(a)
print("Loop-based Tuple:",s)
"""
Size of tuple3
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Loop-based Tuple: ('1', '2', '3')
"""
# 5. Empty tuple
a = ()
print("Empty Tuple:", a)
#Empty Tuple: ()

# 6. Single-element tuple
s= input("Enter a single element: ")
s1 = (s,)
print("Single-element Tuple:", s1)
"""
Enter a single element: 2
Single-element Tuple: ('2',)
"""
# -----------------------
# ⚙️ TUPLE OPERATORS PART
# -----------------------
a = (1, 2, 3, 4, 5)
b = (4, 2, 5, 6, 1)

# 1. Concatenation (c)
c = a + b
print("\nConcatenated tuple :", c)
#Concatenated tuple (c): (1, 2, 3, 4, 5, 4, 2, 5, 6, 1)

# 2. Repetition (r)
r = a * 2
print("Repeated tuple :", r)
#Repeated tuple : (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 3. Membership check (m)
item1 = 3
item2 = 7
m1 = item1 in a
m2 = item2 in b
print(f"Is {item1} in a?:", m1)
print(f"Is {item2} in b?:", m2)
"""
Is 3 in a?: True
Is 7 in b?: False
"""

# 4. Indexing (i)
i = a[2]
print("Element at index 2 in a:", i)
#Element at index 2 in a: 3

# 5. Slicing (s)
s = b[:3]
print("First 3 elements of b:", s)
#First 3 elements of b: (4, 2, 5)

# 6. Length (l)
l1 = len(a)
l2 = len(b)
print("Length of a:", l1)
print("Length of b:", l2)
"""
Length of a: 5
Length of b: 5
"""

# 7. Max, Min, Sum (x, n, u)
x = max(a)
n = min(b)
u = sum(a)
print("Max of a:", x)
print("Min of b:", n)
print("Sum of a:", u)
"""
Max of a: 5
Min of b: 1
Sum of a: 15
"""

# 8. Common elements (o)
o = tuple(i for i in a if i in b)
print("Common elements:", o)
#Common elements: (1, 2, 4, 5)

# 9. Unique elements in a (p)
p = tuple(i for i in a if i not in b)
print("Unique elements in a:", p)
#Unique elements in a: (3,)

# 10. Sorted merged tuple without duplicates (q)
q = tuple(sorted(set(a + b)))
print("Sorted merged tuple without duplicates:", q)
#Sorted merged tuple without duplicates: (1, 2, 3, 4, 5, 6)
