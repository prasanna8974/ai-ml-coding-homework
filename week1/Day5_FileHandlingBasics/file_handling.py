# Write data to a file
with open("notes.txt", "w") as file:
    file.write("Welcome to Python File Handling.\n")
    file.write("I am learning AI and Machine Learning.\n")

print("Data written successfully.")


# Append new data to the file
with open("notes.txt", "a") as file:
    file.write("This is my Week 1 Python homework.\n")

print("Data appended successfully.")


# Read data from the file
with open("notes.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)