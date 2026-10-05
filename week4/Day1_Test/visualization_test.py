# Week 4 - Monday Test
# Visualization and EDA

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [70, 85, 60, 90, 75]
}

df = pd.DataFrame(data)

# Inspect data
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

# Create chart
plt.bar(df["Student"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()

# Summary
print("\nFinding:")
print("The average mark is", df["Marks"].mean())
print("The highest mark is", df["Marks"].max())