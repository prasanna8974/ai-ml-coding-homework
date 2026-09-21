# Week 3 - Monday
# Assignment 3: Bar Chart Program
#
# Question:
# Create a bar chart using categories and values.

import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "Pandas", "NumPy"]
marks = [85, 90, 80, 88]

plt.bar(subjects, marks)

plt.title("Student Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()