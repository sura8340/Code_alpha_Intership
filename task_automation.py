import os

filename = "notes.txt"

with open(filename, "w") as file:
    file.write("Welcome to CodeAlpha Python Internship!\n")
    file.write("This file was created using Python.\n")

print("File created successfully!")

with open(filename, "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)