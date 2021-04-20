import re

# Set up file connection
file_name = input("Enter name of the file:")
if len(file_name) < 1: file_name = "sample-text.txt"
handle = open(file_name)

# Extract all numbers
numbers = re.findall('[0-9]+', handle.read())
integers = []

# Create integer list
for number in numbers:
  integers.append(int(number))

# Once it is finished, sum all numbers in the list
total = sum(integers)

print(total)