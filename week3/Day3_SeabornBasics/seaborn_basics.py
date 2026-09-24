# Week 3 - Wednesday
# Assignment 1: Seaborn Basics
#
# Question:
# Practice count plots, box plots, and pair plots
# using a sample dataset.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create sample student dataset

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John", "Sam"],
    "Department": ["CS", "IT", "CS", "IT", "CS", "IT"],
    "Marks": [90, 85, 78, 92, 88, 80],
    "Age": [26, 24, 25, 23, 27, 24]
}

students = pd.DataFrame(student_data)

print("Student Dataset:")
print(students)


# 1. Count Plot

sns.countplot(x="Department", data=students)

plt.title("Students by Department")
plt.show()


# 2. Box Plot

sns.boxplot(x="Department", y="Marks", data=students)

plt.title("Marks by Department")
plt.show()


# 3. Pair Plot

sns.pairplot(students)

plt.show()