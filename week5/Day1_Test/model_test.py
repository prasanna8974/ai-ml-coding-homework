# Week 5 - Day 1 Test
# Q1: Linear Regression
# Q2: Decision Tree Classification
# Q3: Model Accuracy Evaluation

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Question 1: Predict student marks
hours = [[1], [2], [3], [4], [5], [6]]
marks = [35, 40, 50, 60, 70, 80]

regression = LinearRegression()
regression.fit(hours, marks)

print("Q1 - Predicted Marks:", regression.predict([[7]])[0])


# Question 2: Predict Pass or Fail
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X, y)

result = classifier.predict([[6]])[0]

print("Q2 - Student Result:", "Pass" if result == 1 else "Fail")


# Question 3: Calculate Accuracy
actual = [1, 0, 1, 1, 0, 1]
predicted = [1, 0, 0, 1, 0, 1]

accuracy = accuracy_score(actual, predicted)

print("Q3 - Accuracy:", accuracy)
print("Q3 - Accuracy Percentage:", accuracy * 100, "%")