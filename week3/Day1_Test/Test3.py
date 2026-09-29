# Week 3 - Monday
# Coding Test - Different Version
#
# Topics:
# 1. NumPy Arrays
# 2. Basic Statistics
# 3. Pandas DataFrame
# 4. Data Filtering

import numpy as np
import pandas as pd


# 1. Create NumPy array of salaries

salaries = np.array([
    45000,
    52000,
    61000,
    58000,
    72000,
    68000
])

print("SALARY ARRAY:")
print(salaries)


# 2. Basic Statistics

print("\nSALARY STATISTICS:")

print("Average Salary:", np.mean(salaries))
print("Median Salary:", np.median(salaries))
print("Highest Salary:", np.max(salaries))
print("Lowest Salary:", np.min(salaries))
print("Standard Deviation:", np.std(salaries))


# 3. Create Employee DataFrame

employee_data = {
    "Employee": [
        "Alex",
        "David",
        "Emma",
        "Sophia",
        "Daniel",
        "Olivia"
    ],

    "Department": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "Finance",
        "IT"
    ],

    "Experience": [
        2,
        4,
        6,
        3,
        8,
        5
    ],

    "Salary": [
        45000,
        52000,
        61000,
        58000,
        72000,
        68000
    ]
}

employees = pd.DataFrame(employee_data)


# 4. Display DataFrame

print("\nEMPLOYEE DATA:")
print(employees)


# 5. Filter employees with salary above 60000

print("\nEMPLOYEES WITH SALARY ABOVE 60000:")

high_salary = employees[
    employees["Salary"] > 60000
]

print(high_salary)


# 6. Filter IT employees

print("\nIT DEPARTMENT EMPLOYEES:")

it_employees = employees[
    employees["Department"] == "IT"
]

print(it_employees)


# 7. Employees with more than 5 years experience

print("\nEMPLOYEES WITH MORE THAN 5 YEARS EXPERIENCE:")

experienced = employees[
    employees["Experience"] > 5
]

print(experienced)


# 8. Average salary from DataFrame

print("\nAVERAGE EMPLOYEE SALARY:")

print(employees["Salary"].mean())