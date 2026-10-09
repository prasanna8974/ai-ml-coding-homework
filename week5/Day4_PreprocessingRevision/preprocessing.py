# Week 5 - Thursday
# Assignment 1: Data Preprocessing Revision

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create dataset
data = {
    "Age": [22, 25, None, 30, 35, 40, 45, 50],
    "Salary": [30000, 35000, 40000, 45000,
               50000, 60000, 70000, 80000],
    "Department": ["IT", "HR", "IT", "HR",
                   "IT", "HR", "IT", "HR"],
    "Promoted": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Separate features and target
X = df.drop("Promoted", axis=1)
y = df["Promoted"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Handle missing values using training mean
mean_age = X_train["Age"].mean()

X_train = X_train.copy()
X_test = X_test.copy()

X_train["Age"] = X_train["Age"].fillna(mean_age)
X_test["Age"] = X_test["Age"].fillna(mean_age)

# Encode categorical data
X_train = pd.get_dummies(X_train, columns=["Department"])
X_test = pd.get_dummies(X_test, columns=["Department"])

X_test = X_test.reindex(
    columns=X_train.columns, fill_value=0
)

# Scale numerical features
scaler = StandardScaler()

columns = ["Age", "Salary"]

X_train[columns] = scaler.fit_transform(X_train[columns])
X_test[columns] = scaler.transform(X_test[columns])

print("\nProcessed Training Data:")
print(X_train)

print("\nProcessed Testing Data:")
print(X_test)