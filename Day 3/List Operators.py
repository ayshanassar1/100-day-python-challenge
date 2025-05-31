# Creating a list
colors = ["red", "green", "blue"]
print(colors)  
# Output:['red','green', 'blue']

# Append element
colors.append("yellow")
print("After append:",colors)
#After append: ['red', 'green', 'blue', 'yellow']

#insert element
colors.insert(1, "orange")
print("After Insert:",colors)
#After Insert: ['red', 'orange', 'green', 'blue', 'yellow']

#remove element
colors.remove("green")
print("After remove:",colors)
#After remove: ['red', 'orange', 'blue', 'yellow']

# Indexing, Slicing
print("First color:", colors[0])  
# Output: First color: red

print("Last two colors:", colors[-2:])  
# Output: Last two colors: ['blue', 'yellow']

# List Comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)  
# Output: Squares: [1, 4, 9, 16, 25]

# Looping through list
for color in colors:
    print("Color:", color)
# Output:
# Color: red
# Color: orange
# Color: blue
# Color: yellow

# Check existence
print("blue" in colors)  
# Output:True

# Count 
print("Count of 'red':", colors.count("red"))  
# Output: Count of 'red': 1

#Length
print("Length of list:", len(colors))  
# Output: Length of list: 4

