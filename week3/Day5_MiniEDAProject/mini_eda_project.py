# Week 3 - Friday
# Mini EDA Project
#
# Question:
# Perform Exploratory Data Analysis (EDA) on a sample CSV dataset.
# Check data quality, calculate statistics, analyze categories,
# create charts, and write important findings.

import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------

students = pd.read_csv("student_data.csv")

print("STUDENT DATASET")
print(students)


# ------------------------------------------------
# 2. BASIC DATASET INFORMATION
# ------------------------------------------------

print("\nFIRST 5 ROWS")
print(students.head())

print("\nDATASET SHAPE")
print(students.shape)

print("\nCOLUMN NAMES")
print(students.columns)

print("\nDATA TYPES")
print(students.dtypes)


# ------------------------------------------------
# 3. DATA QUALITY CHECK
# ------------------------------------------------

print("\nMISSING VALUES")
print(students.isnull().sum())

print("\nDUPLICATE ROWS")
print(students.duplicated().sum())


# ------------------------------------------------
# 4. BASIC STATISTICS
# ------------------------------------------------

print("\nSTATISTICAL SUMMARY")
print(students.describe())

print("\nAVERAGE MARKS")
print(students["Marks"].mean())

print("\nMEDIAN MARKS")
print(students["Marks"].median())

print("\nHIGHEST MARKS")
print(students["Marks"].max())

print("\nLOWEST MARKS")
print(students["Marks"].min())


# ------------------------------------------------
# 5. CATEGORICAL ANALYSIS
# ------------------------------------------------

print("\nSTUDENTS BY DEPARTMENT")
print(students["Department"].value_counts())

print("\nAVERAGE MARKS BY DEPARTMENT")
print(
    students.groupby("Department")["Marks"].mean()
)


# ------------------------------------------------
# 6. FILTERING
# ------------------------------------------------

print("\nSTUDENTS WITH MARKS ABOVE 80")
print(students[students["Marks"] > 80])


# ------------------------------------------------
# 7. CORRELATION ANALYSIS
# ------------------------------------------------

print("\nCORRELATION")
print(
    students[
        ["Study_Hours", "Attendance", "Marks"]
    ].corr()
)


# ------------------------------------------------
# 8. BAR CHART
# ------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    students["Name"],
    students["Marks"]
)

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()


# ------------------------------------------------
# 9. HISTOGRAM
# ------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    students["Marks"],
    bins=5
)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# ------------------------------------------------
# 10. SCATTER PLOT
# ------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    students["Study_Hours"],
    students["Marks"]
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.tight_layout()
plt.show()


# ------------------------------------------------
# 11. FINDINGS
# ------------------------------------------------

print("\nEDA FINDINGS")

print("1. Average Marks:",
      students["Marks"].mean())

print("2. Highest Marks:",
      students["Marks"].max())

print("3. Lowest Marks:",
      students["Marks"].min())

print("4. Students Scoring Above 80:",
      len(students[students["Marks"] > 80]))

print(
    "5. The sample data shows that students with more "
    "study hours generally have higher marks."
)


print("\nMini EDA Project Completed Successfully!")