# Week 3 - Tuesday
# Assignment 2: Multiple Plot Practice
#
# Question:
# Create multiple separate charts and understand
# the purpose of each chart.

import matplotlib.pyplot as plt


# Chart 1: Line Chart
# Used to show changes or trends.

days = [1, 2, 3, 4, 5]
marks = [60, 68, 75, 82, 90]

plt.figure()
plt.plot(days, marks)

plt.title("Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")

plt.show()


# Chart 2: Bar Chart
# Used to compare different categories.

subjects = ["Python", "SQL", "Pandas", "NumPy"]
scores = [85, 90, 80, 88]

plt.figure()
plt.bar(subjects, scores)

plt.title("Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Score")

plt.show()


# Chart 3: Scatter Plot
# Used to observe the relationship between two variables.

study_hours = [1, 2, 3, 4, 5]
exam_marks = [50, 60, 70, 80, 90]

plt.figure()
plt.scatter(study_hours, exam_marks)

plt.title("Study Hours vs Exam Marks")
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")

plt.show()