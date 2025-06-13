filename = "example.txt"

# 1. Create and Write to File (will overwrite if exists)
with open(filename, "w") as file:
    file.write("Hello, this is a file.\n")
    file.write("This is the second line.\n")
print("File created and written.")

# Output:
# File created and written.

# 2. Read Entire Content
try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFull Content:\n", content)
except FileNotFoundError:
    print("File not found when reading.")

# Output:
# Full Content:
# Hello, this is a file.
# This is the second line.

# 3. Read Line by Line
print("\nReading line by line:")
try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found when reading line-by-line.")

# Output:
# Reading line by line:
# Hello, this is a file.
# This is the second line.

# 4. Append to File
with open(filename, "a") as file:
    file.write("This line is added later.\n")
    file.write("Another appended line.\n")
print("Appended new lines.")

# Output:
# Appended new lines.

# 5. Read as List of Lines
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print("\nFile as list of lines:")
        print(lines)
except FileNotFoundError:
    print("File not found when reading lines as list.")

# Output:
# File as list of lines:
# ['Hello, this is a file.\n', 'This is the second line.\n', 
#  'This line is added later.\n', 'Another appended line.\n']

