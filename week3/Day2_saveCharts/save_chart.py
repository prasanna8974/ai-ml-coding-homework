# Week 3 - Tuesday
# Assignment 4: Save Charts to File
#
# Question:
# Create a chart using Matplotlib
# and save the chart as an image file.

import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "Pandas", "NumPy"]
marks = [85, 90, 80, 88]

# Create bar chart
plt.bar(subjects, marks)

# Add title and labels
plt.title("Student Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Save chart as an image
plt.savefig("student_marks_chart.png")

# Display chart
plt.show()

print("Chart saved successfully!")