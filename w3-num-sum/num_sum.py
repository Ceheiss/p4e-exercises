import re

print("Hello World")

# Set up file connection
file_name = input("Enter name of the file:")
if len(file_name) < 1: file_name = "sample-text.txt"
handle = open(file_name)

print(handle.read())
