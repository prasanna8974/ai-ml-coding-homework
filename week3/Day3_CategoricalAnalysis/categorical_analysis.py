# Week 3 - Wednesday
# Assignment 4: Categorical Analysis
#
# Question:
# Analyze categorical data using counts and averages.
# Visualize the results using a bar chart.

import pandas as pd
import matplotlib.pyplot as plt

# Create sample student dataset
student_data = {
    "Department": ["CS", "IT", "CS", "IT", "CS", "IT"],
    "Marks": [90, 75, 85, 80, 95, 70]
}

students = pd.DataFrame(student_data)

print("Student Data:")
print(students)

# Count students in each department
department_count = students["Department"].value_counts()

print("\nNumber of Students in Each Department:")
print(department_count)

# Calculate average marks by department
average_marks = students.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(average_marks)

# Create bar chart
average_marks.plot(kind="bar")

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.show()