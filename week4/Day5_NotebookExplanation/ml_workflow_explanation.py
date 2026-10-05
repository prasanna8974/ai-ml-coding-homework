# Week 4 - Friday
# Assignment 2: ML Workflow Explanation
#
# This program explains the main steps
# involved in a Machine Learning project.

print("MACHINE LEARNING WORKFLOW")


# --------------------------------
# Step 1: Data Loading
# --------------------------------

print("\n1. DATA LOADING")

print(
    "Data loading means reading or collecting "
    "the dataset that will be used for the ML project."
)

print(
    "Example: We can load data from a CSV file "
    "using Pandas."
)


# --------------------------------
# Step 2: Data Preprocessing
# --------------------------------

print("\n2. DATA PREPROCESSING")

print(
    "Preprocessing means preparing the data "
    "before giving it to the machine learning model."
)

print(
    "It can include handling missing values, "
    "removing duplicates, selecting features, "
    "and scaling numerical features."
)


# --------------------------------
# Step 3: Features and Target
# --------------------------------

print("\n3. FEATURES AND TARGET")

print(
    "Features are the input variables used "
    "by the model to make predictions."
)

print(
    "The target is the value or class "
    "that the model is trying to predict."
)

print(
    "Example: Study_Hours and Attendance are features, "
    "while Pass is the target."
)


# --------------------------------
# Step 4: Train-Test Split
# --------------------------------

print("\n4. TRAIN-TEST SPLIT")

print(
    "The dataset is divided into training "
    "and testing data."
)

print(
    "Training data is used to train the model."
)

print(
    "Testing data is used to evaluate the model "
    "on data it did not train on."
)


# --------------------------------
# Step 5: Model Training
# --------------------------------

print("\n5. MODEL TRAINING")

print(
    "During training, the model learns patterns "
    "from the training data."
)

print(
    "In Scikit-learn, model.fit() is commonly "
    "used to train the model."
)


# --------------------------------
# Step 6: Prediction
# --------------------------------

print("\n6. PREDICTION")

print(
    "After training, the model can make predictions "
    "on new or test data."
)

print(
    "In Scikit-learn, model.predict() "
    "is used to generate predictions."
)


# --------------------------------
# Step 7: Model Evaluation
# --------------------------------

print("\n7. MODEL EVALUATION")

print(
    "Model evaluation checks how well "
    "the model performs."
)

print(
    "For classification, we can use accuracy, "
    "confusion matrix, precision, recall, "
    "and F1-score."
)


# --------------------------------
# Final Workflow
# --------------------------------

print("\nCOMPLETE ML WORKFLOW:")

print(
    "Data Loading -> Preprocessing -> "
    "Features and Target -> Train-Test Split -> "
    "Training -> Prediction -> Evaluation"
)