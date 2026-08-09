#!/usr/bin/env python3
"""Generate student demo Jupyter notebooks covering all 3-day course material."""

import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from pathlib import Path

OUT_DIR = Path(__file__).parent


def write_notebook(name, cells):
    """Build and save a notebook from a list of cells."""
    nb = new_notebook(cells=cells)
    nb["metadata"]["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    path = OUT_DIR / name
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Created {path}")


def md(text):
    return new_markdown_cell(text)


def code(text):
    return new_code_cell(text)


# ========================================================================
# DAY 1: Python + Pandas
# ========================================================================
day1_cells = [
    md("""# Day 1 Demo Notebook: Python + Pandas

Welcome to the 3-Day Data Science Prep Course. This notebook follows the Day 1 materials: **Python basics + Pandas data wrangling**.

**Learning Objectives**
- Write basic Python: variables, lists, dictionaries, loops, functions
- Load a CSV file using Pandas
- Select, filter, sort, and group data
- Handle missing values and create new columns
- Save a cleaned dataset

**How to use this notebook:**
1. Run each cell with `Shift + Enter`.
2. Change values and re-run cells to experiment.
3. If you get stuck, read the error carefully — debugging is the most important skill."""),

    md("""## Part 1: Python Crash Course

A **variable** is a labeled box that stores a value. Python figures out the type automatically."""),

    code("""# Variables and data types
name = "Alice"
age = 18
height = 1.65
is_student = True

print(name, age, height, is_student)
print("Types:", type(name), type(age), type(height), type(is_student))"""),

    md("""### Lists
- Ordered collection of items
- `scores[0]` gets the first item
- `scores[-1]` gets the last item
- `append()` adds an item
- `len()` gives the length"""),

    code("""# Lists
scores = [85, 90, 78, 92]
print("First score:", scores[0])
print("Last score:", scores[-1])
scores.append(88)
print("After append:", scores)
print("Length:", len(scores))"""),

    md("""### Dictionaries
Dictionaries store key-value pairs."""),

    code("""# Dictionaries
student = {
    "name": "Alice",
    "age": 18,
    "major": "Data Science"
}
print(student["name"])
student["gpa"] = 3.8
print(student)"""),

    md("""### Conditions and Loops"""),

    code("""# Conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)

# For loop
for s in scores:
    print(s)

# While loop
n = 0
while n < 5:
    print(n)
    n += 1"""),

    md("""### Functions
Functions are reusable blocks of code."""),

    code("""# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print("Average score:", calculate_average(scores))"""),

    md("""## Part 2: Python Exercises

Try these yourself. Add new code cells below each exercise."""),

    md("""### Exercise 1: Variables
Create variables for your name, age, and whether you like data science. Print them all."""),

    code("""# Your code here

"""),

    md("""### Exercise 2: List Operations
Given `prices = [12.5, 18.0, 7.5, 25.0, 10.0]`:
- Print the first price
- Print the last price
- Add a new price of 15.0
- Print the length of the list"""),

    code("""prices = [12.5, 18.0, 7.5, 25.0, 10.0]
# Your code here

"""),

    md("""### Exercise 3: Loop Practice
Print every price with a 10% discount applied."""),

    code("""# Your code here

"""),

    md("""### Exercise 4: Function Practice
Write a function `calculate_average(numbers)` that returns the average of a list."""),

    code("""# Your code here

"""),

    md("""### Exercise 5: Dictionary Practice
Create a dictionary for a book with keys: `title`, `author`, `year`. Print each value."""),

    code("""# Your code here

"""),

    md("""## Part 3: Introduction to Pandas

Pandas is the industry-standard library for working with data tables in Python. It is like Excel or Google Sheets, but with code."""),

    code("""import pandas as pd

# Load the Titanic dataset from a URL
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)"""),

    md("""### Inspecting a DataFrame
Use these commands to understand your data quickly."""),

    code("""# First 5 rows
df.head()"""),

    code("""# Last 5 rows
df.tail()"""),

    code("""# Column names
print(df.columns.tolist())"""),

    code("""# Data types and missing values
df.info()"""),

    code("""# Summary statistics for numeric columns
df.describe()"""),

    md("""## Part 4: Selecting and Filtering"""),

    md("""### Selecting Columns"""),

    code("""# One column -> Series
df["Name"].head()"""),

    code("""# Multiple columns -> DataFrame
df[["Name", "Age", "Sex", "Survived"]].head()"""),

    md("""### Selecting Rows by Position"""),

    code("""# First row
df.iloc[0]"""),

    code("""# First 5 rows
df.iloc[0:5]"""),

    md("""### Filtering Rows by Condition"""),

    code("""# Passengers older than 30
df[df["Age"] > 30].head()"""),

    code("""# Female passengers only
df[df["Sex"] == "female"].head()"""),

    code("""# Multiple conditions
rich_females = df[(df["Sex"] == "female") & (df["Fare"] > 50)]
rich_females.head()"""),

    md("""### Sorting"""),

    code("""# Oldest first
df.sort_values("Age", ascending=False).head()"""),

    code("""# Sort by class then age
df.sort_values(["Pclass", "Age"]).head()"""),

    md("""## Part 5: Transformations and Aggregation"""),

    md("""### Adding New Columns"""),

    code("""# Family size = siblings + parents + self
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df[["SibSp", "Parch", "FamilySize"]].head()"""),

    md("""### Dropping Columns"""),

    code("""# Drop Cabin column if it exists (too many missing values)
if "Cabin" in df.columns:
    df = df.drop(columns=["Cabin"])
print("Columns after drop:", df.columns.tolist())"""),

    md("""### Handling Missing Values"""),

    code("""# Count missing values per column
df.isnull().sum()"""),

    code("""# Fill missing ages with the median age
median_age = df["Age"].median()
print("Median age:", median_age)
df["Age"] = df["Age"].fillna(median_age)

# Verify there are no missing ages now
df["Age"].isnull().sum()"""),

    md("""### Groupby and Aggregation"""),

    code("""# Average age by passenger class
df.groupby("Pclass")["Age"].mean()"""),

    code("""# Survival rate by sex
df.groupby("Sex")["Survived"].mean()"""),

    code("""# Multiple aggregations at once
df.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "mean",
    "Survived": "mean"
})"""),

    md("""## Part 6: Save the Cleaned Dataset"""),

    code("""# Save to CSV
output_path = "cleaned_titanic.csv"
df.to_csv(output_path, index=False)
print(f"Saved cleaned data to {output_path}")"""),

    md("""## Day 1 Wrap-Up

**What we learned today:**
- Python basics: variables, lists, dicts, loops, functions
- Pandas DataFrames
- Loading, filtering, transforming, grouping data
- Saving cleaned data

**Homework:**
1. Rebuild this notebook from scratch (no copy-paste).
2. Try grouping by two columns: `df.groupby(["Sex", "Pclass"])["Survived"].mean()`
3. Read the Pandas cheatsheet.

**Next:** Day 2 covers EDA, visualization, and statistics."""),
]

# ========================================================================
# DAY 2: EDA + Visualization + Statistics
# ========================================================================
day2_cells = [
    md("""# Day 2 Demo Notebook: EDA + Visualization + Statistics

This notebook follows the Day 2 materials: **exploratory data analysis, descriptive statistics, and visualization with Matplotlib and Seaborn**.

**Learning Objectives**
- Perform exploratory data analysis using Pandas
- Compute and interpret descriptive statistics
- Understand correlation and basic probability
- Create common charts with Matplotlib and Seaborn
- Combine statistics and visualization into a short EDA report
"""),

    code("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This line makes charts appear in the notebook
%matplotlib inline

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)"""),

    md("""## Part 1: Exploratory Data Analysis (EDA)

EDA = Exploratory Data Analysis. The goal is to understand the data before building models.

**The EDA mindset:**
1. What is the shape of the data?
2. What does each column mean?
3. Are there missing values?
4. What are the distributions?
5. Are there relationships between variables?"""),

    code("""# Basic overview
print("Rows, Columns:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nInfo:")
df.info()
print("\nDescribe:")
df.describe()"""),

    code("""# Value counts for categorical columns
print("Sex counts:")
print(df["Sex"].value_counts())
print("\nClass counts:")
print(df["Pclass"].value_counts())
print("\nEmbarked counts:")
print(df["Embarked"].value_counts())"""),

    code("""# Missing values
print("Missing values per column:")
print(df.isnull().sum())
print("\nPercentage missing:")
print(df.isnull().sum() / len(df) * 100)"""),

    code("""# Unique values
print("Unique classes:", df["Pclass"].nunique())
print("Unique classes list:", df["Pclass"].unique())"""),

    md("""## Part 2: Descriptive Statistics"""),

    code("""# Compute statistics for Age
print("Mean age:", df["Age"].mean())
print("Median age:", df["Age"].median())
print("Std dev age:", df["Age"].std())
print("Min age:", df["Age"].min())
print("Max age:", df["Age"].max())"""),

    md("""### Distribution, Outliers, and Correlation

- **Mean**: average
- **Median**: middle value (less affected by outliers)
- **Standard deviation**: how spread out the data is
- **Outliers**: values much higher or lower than most of the data
- **Correlation**: measures how two variables move together (-1 to +1)

**Important**: Correlation is not causation!"""),

    code("""# Correlation matrix for selected numeric columns
# First add FamilySize if it doesn't exist
if "FamilySize" not in df.columns:
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

corr = df[["Age", "Fare", "Pclass", "Survived", "FamilySize"]].corr()
print(corr)"""),

    code("""# Basic probability
print("Overall survival rate:", df["Survived"].mean())
print("Female survival rate:", df[df["Sex"] == "female"]["Survived"].mean())
print("Male survival rate:", df[df["Sex"] == "male"]["Survived"].mean())"""),

    md("""## Part 3: Matplotlib Fundamentals"""),

    md("""### Line Plot"""),

    code("""# Simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()"""),

    md("""### Bar Chart"""),

    code("""# Survival counts
survival_counts = df["Survived"].value_counts().sort_index()
plt.bar(["Died", "Survived"], survival_counts)
plt.title("Survival Counts")
plt.ylabel("Number of passengers")
plt.show()"""),

    md("""### Histogram"""),

    code("""# Age distribution
plt.hist(df["Age"].dropna(), bins=20, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()"""),

    md("""### Scatter Plot"""),

    code("""# Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()"""),

    md("""## Part 4: Better Charts with Seaborn"""),

    md("""Seaborn is built on top of Matplotlib and makes prettier, more statistical charts with less code."""),

    md("""### Count Plot"""),

    code("""plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex")
plt.title("Count by Sex")
plt.show()"""),

    md("""### Boxplot"""),

    code("""plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Pclass", y="Age")
plt.title("Age Distribution by Passenger Class")
plt.show()"""),

    md("""### Histogram with KDE (density curve)"""),

    code("""plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution with Density")
plt.show()"""),

    md("""### Correlation Heatmap"""),

    code("""plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()"""),

    md("""### Pairplot

A pairplot shows relationships between multiple numeric variables at once."""),

    code("""sns.pairplot(df[["Age", "Fare", "Survived"]], hue="Survived")
plt.show()"""),

    md("""## Part 5: Build an EDA Report

Use this structure for your own EDA notebook.

### Section 1: Introduction
- What dataset are you using?
- What question are you trying to answer?

### Section 2: Data Overview
- Shape, columns, missing values
- Summary statistics

### Section 3: Univariate Analysis
- Histograms or bar charts of single variables

### Section 4: Bivariate Analysis
- Charts comparing two variables

### Section 5: Correlation
- Correlation heatmap

### Section 6: Conclusions
- 3–5 bullet points summarizing key findings"""),

    md("""### Example Mini-Report"""),

    code("""# Section 2: Data overview
print("Dataset: Titanic passenger records")
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("\nSummary statistics:")
df.describe()"""),

    code("""# Section 3: Univariate analysis - survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived")
plt.title("Survival Counts")
plt.show()"""),

    code("""# Section 3: Univariate analysis - age distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution")
plt.show()"""),

    code("""# Section 4: Bivariate analysis - survival by sex
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Sex")
plt.show()"""),

    code("""# Section 4: Bivariate analysis - fare by class
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Pclass", y="Fare")
plt.title("Fare by Passenger Class")
plt.show()"""),

    code("""# Section 5: Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()"""),

    md("""### Section 6: Example Conclusions

1. About 38% of passengers survived overall.
2. Female passengers had a much higher survival rate than male passengers.
3. First-class passengers paid much higher fares on average.
4. There is a negative correlation between Pclass and Survived (lower class number = higher survival).
5. Most passengers were between 20 and 40 years old."""),

    md("""## Day 2 Wrap-Up

**What we learned today:**
- EDA mindset and Pandas tools
- Descriptive statistics: mean, median, std, correlation
- Probability basics
- Matplotlib: line, bar, histogram, scatter
- Seaborn: countplot, boxplot, histplot, heatmap, pairplot
- How to build an EDA report

**Homework:**
1. Add 2 more charts to your EDA report.
2. Write a one-paragraph summary of your findings.
3. Read the Matplotlib and Seaborn cheatsheets.

**Next:** Day 3 covers machine learning and the capstone project."""),
]

# ========================================================================
# DAY 3: Machine Learning
# ========================================================================
day3_cells = [
    md("""# Day 3 Demo Notebook: Machine Learning

This notebook follows the Day 3 materials: **machine learning concepts, model training, evaluation, and capstone preparation**.

**Learning Objectives**
- Explain what machine learning is in plain language
- Distinguish supervised from unsupervised learning
- Split data into training and testing sets
- Build a classification model using scikit-learn
- Evaluate a model with accuracy and confusion matrix
- Complete an end-to-end data science project
"""),

    md("""## Part 1: Machine Learning Concepts

### What is Machine Learning?
- Traditional programming: human writes rules
- Machine learning: computer learns patterns from data
- Input data + answers → model → predictions on new data

### The ML Recipe
1. Collect data
2. Prepare / clean data
3. Choose a model
4. Train the model on training data
5. Test the model on new data
6. Evaluate and improve

### Supervised vs Unsupervised
- **Supervised learning**: we have labeled examples (input + correct answer)
  - Classification: predict a category (survived/died, spam/not spam)
  - Regression: predict a number (house price, temperature)
- **Unsupervised learning**: no labels, model finds patterns/groups
  - Example: customer segmentation

### Features and Target
- **Features (X)**: input columns used for prediction
- **Target (y)**: the value we want to predict
- In Titanic: features = Age, Sex, Fare, Pclass; target = Survived

### Overfitting vs Underfitting
- **Underfitting**: model too simple, misses patterns
- **Overfitting**: model memorizes training data, fails on new data
- Goal: balance between the two"""),

    md("""## Part 2: Prepare Data for Machine Learning"""),

    code("""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# Select simple features
features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

print("Features (X) shape:", X.shape)
print("Target (y) shape:", y.shape)"""),

    code("""# Handle missing values
X["Age"] = X["Age"].fillna(X["Age"].median())
print("Missing values after fill:\n", X.isnull().sum())"""),

    code("""# Convert text to numbers
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})
print(X.head())"""),

    md("""## Part 3: Train/Test Split"""),

    code("""# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)"""),

    md("""## Part 4: Train a Model"""),

    code("""# Create and train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained!")"""),

    md("""## Part 5: Make Predictions and Evaluate"""),

    code("""# Predict on the test set
predictions = model.predict(X_test)
print("First 10 predictions:", predictions[:10])
print("First 10 actual:", y_test.values[:10])"""),

    code("""# Accuracy: percentage of correct predictions
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")"""),

    code("""# Confusion matrix
# Rows = actual, Columns = predicted
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)
print("\nPredicted: Died  Survived")
print(f"Actual Died:    {cm[0,0]:3}    {cm[0,1]:3}")
print(f"Actual Survived:{cm[1,0]:3}    {cm[1,1]:3}")"""),

    code("""# Detailed classification report
print(classification_report(y_test, predictions, target_names=["Died", "Survived"]))"""),

    md("""## Part 6: Feature Importance"""),

    code("""# Coefficients show the impact of each feature
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values("Coefficient", ascending=False)

print(importance)"""),

    code("""# Visualize feature importance
plt.figure(figsize=(8, 5))
sns.barplot(data=importance, x="Coefficient", y="Feature", orient="h")
plt.title("Feature Importance (Logistic Regression Coefficients)")
plt.show()"""),

    md("""## Part 7: Capstone Preparation

Choose one of these projects to complete today:
- **Titanic Survival Prediction** (classification)
- **Iris Flower Classification** (multi-class classification)
- **House Price Prediction** (regression)

A complete project should include:
1. Load and explore the data
2. Clean and prepare features
3. Create at least 3 visualizations
4. Build a machine learning model
5. Evaluate the model
6. Write conclusions
7. Save notebook and upload to GitHub"""),

    md("""## Part 8: GitHub Upload Instructions

1. Go to github.com and sign in.
2. Click **New repository**.
3. Name it `data-science-prep-projects`.
4. Make it public.
5. Click **Upload files**.
6. Drag and drop your `.ipynb` notebook files.
7. Add a README.md describing the projects.

You have now done real data science!"""),
]

# ========================================================================
# CAPSTONE: Titanic Survival Prediction
# ========================================================================
titanic_cells = [
    md("""# Capstone Project: Titanic Survival Prediction

**Project Type:** Classification  
**Dataset:** Titanic passenger records  
**Goal:** Predict whether a passenger survived or died.

This notebook is a complete end-to-end project. Follow along, then modify it to make it your own."""),

    md("""## 1. Import Libraries"""),

    code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

%matplotlib inline"""),

    md("""## 2. Load and Explore the Data"""),

    code("""url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)
df.head()"""),

    code("""# Data overview
print("Columns:", df.columns.tolist())
print("\nInfo:")
df.info()
print("\nDescribe:")
df.describe()"""),

    code("""# Missing values
print(df.isnull().sum())
print("\nPercentage missing:")
print(df.isnull().sum() / len(df) * 100)"""),

    md("""## 3. Exploratory Data Analysis"""),

    code("""# Survival counts
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived")
plt.title("Survival Counts")
plt.xticks([0, 1], ["Died", "Survived"])
plt.show()"""),

    code("""# Survival by sex
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Sex")
plt.legend(["Died", "Survived"])
plt.show()"""),

    code("""# Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution")
plt.show()"""),

    code("""# Fare by class
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Pclass", y="Fare")
plt.title("Fare by Passenger Class")
plt.show()"""),

    code("""# Correlation heatmap
if "FamilySize" not in df.columns:
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

numeric_cols = ["Age", "Fare", "Pclass", "SibSp", "Parch", "FamilySize", "Survived"]
plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()"""),

    md("""## 4. Prepare Features"""),

    code("""# Select features
features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
X = df[features].copy()
y = df["Survived"]

# Fill missing ages with median
X["Age"] = X["Age"].fillna(X["Age"].median())

# Convert sex to numbers
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})

print("Missing values:")
print(X.isnull().sum())
print("\nFirst 5 rows:")
print(X.head())"""),

    md("""## 5. Split Data"""),

    code("""X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)"""),

    md("""## 6. Train Models"""),

    code("""# Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))"""),

    code("""# Decision Tree
dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))"""),

    md("""## 7. Evaluate the Best Model"""),

    code("""# Use logistic regression for detailed evaluation
predictions = lr_pred

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=["Died", "Survived"]))"""),

    code("""# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": lr_model.coef_[0]
}).sort_values("Coefficient", ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=importance, x="Coefficient", y="Feature")
plt.title("Feature Importance")
plt.show()"""),

    md("""## 8. Conclusions

Write your findings here:

1. What was your accuracy?
2. Which features were most important?
3. What would you try next? (e.g., use title from name, fill missing values differently, try more models)
4. What did you learn about the Titanic data?"""),

    code("""# Save the cleaned dataset for reference
# df.to_csv("titanic_cleaned.csv", index=False)
print("Project complete!")"""),
]

# ========================================================================
# CAPSTONE: Iris Flower Classification
# ========================================================================
iris_cells = [
    md("""# Capstone Project: Iris Flower Classification

**Project Type:** Multi-class Classification  
**Dataset:** Iris flower measurements (built into scikit-learn)  
**Goal:** Predict the species of an iris flower from its measurements.

This is one of the most famous beginner datasets in machine learning."""),

    md("""## 1. Import Libraries"""),

    code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

%matplotlib inline"""),

    md("""## 2. Load the Data"""),

    code("""iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="species")

# Map target numbers to species names
species_map = {i: name for i, name in enumerate(iris.target_names)}
y = y.map(species_map)

df = pd.concat([X, y], axis=1)
print("Shape:", df.shape)
df.head()"""),

    code("""# Overview
print(df.info())
print("\nSpecies counts:")
print(df["species"].value_counts())"""),

    md("""## 3. Exploratory Data Analysis"""),

    code("""# Species counts
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="species")
plt.title("Species Counts")
plt.show()"""),

    code("""# Distribution of sepal length
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="sepal length (cm)", kde=True, hue="species")
plt.title("Sepal Length Distribution by Species")
plt.show()"""),

    code("""# Sepal length vs sepal width
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="sepal length (cm)", y="sepal width (cm)", hue="species")
plt.title("Sepal Length vs Sepal Width")
plt.show()"""),

    code("""# Pairplot: shows all pairwise relationships
sns.pairplot(df, hue="species")
plt.show()"""),

    md("""## 4. Prepare Data for ML"""),

    code("""X = df.drop("species", axis=1)
y = df["species"]

print("Features shape:", X.shape)
print("Target shape:", y.shape)"""),

    md("""## 5. Train/Test Split"""),

    code("""X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)"""),

    md("""## 6. Train Models"""),

    code("""# Logistic Regression
lr_model = LogisticRegression(max_iter=200)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))"""),

    code("""# Decision Tree
dt_model = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))"""),

    md("""## 7. Evaluate the Model"""),

    code("""predictions = lr_pred

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))"""),

    code("""# Confusion matrix heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(
    confusion_matrix(y_test, predictions, labels=iris.target_names),
    annot=True,
    fmt="d",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names,
    cmap="Blues",
)
plt.title("Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()"""),

    md("""## 8. Conclusions

1. Which model performed best?
2. Which features seem most useful for distinguishing species?
3. Were there any flowers that the model confused?
4. What would you try next?"""),

    code("""print("Iris project complete!")"""),
]

# ========================================================================
# CAPSTONE: House Price Prediction
# ========================================================================
house_cells = [
    md("""# Capstone Project: California House Price Prediction

**Project Type:** Regression  
**Dataset:** California Housing (built into scikit-learn)  
**Goal:** Predict the median house value for California districts.

This project is great for practicing regression, where the target is a continuous number instead of a category."""),

    md("""## 1. Import Libraries"""),

    code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

%matplotlib inline"""),

    md("""## 2. Load the Data"""),

    code("""housing = fetch_california_housing(as_frame=True)
df = housing.frame.copy()

print("Shape:", df.shape)
df.head()"""),

    code("""# Data overview
print(df.info())
print("\nDescribe:")
print(df.describe())"""),

    md("""## 3. Exploratory Data Analysis"""),

    code("""# Distribution of target variable: median house value
plt.figure(figsize=(8, 5))
sns.histplot(df["MedHouseValue"], kde=True, bins=50)
plt.title("Distribution of Median House Value")
plt.xlabel("Median House Value ($100,000s)")
plt.show()"""),

    code("""# Median income vs house value
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="MedInc", y="MedHouseValue", alpha=0.3)
plt.title("Median Income vs Median House Value")
plt.show()"""),

    code("""# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()"""),

    md("""## 4. Prepare Data for ML"""),

    code("""X = df.drop("MedHouseValue", axis=1)
y = df["MedHouseValue"]

print("Features:", X.columns.tolist())
print("Features shape:", X.shape)
print("Target shape:", y.shape)"""),

    md("""## 5. Train/Test Split"""),

    code("""X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)"""),

    md("""## 6. Train Regression Models"""),

    code("""# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

print("Linear Regression:")
print("  RMSE:", np.sqrt(mean_squared_error(y_test, lr_pred)))
print("  MAE:", mean_absolute_error(y_test, lr_pred))
print("  R2:", r2_score(y_test, lr_pred))"""),

    code("""# Decision Tree Regressor
dt_model = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

print("Decision Tree Regressor:")
print("  RMSE:", np.sqrt(mean_squared_error(y_test, dt_pred)))
print("  MAE:", mean_absolute_error(y_test, dt_pred))
print("  R2:", r2_score(y_test, dt_pred))"""),

    md("""## 7. Evaluate the Best Model"""),

    code("""predictions = lr_pred

plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted House Values")
plt.show()"""),

    code("""# Residual plot
residuals = y_test - predictions
plt.figure(figsize=(8, 5))
sns.histplot(residuals, kde=True, bins=50)
plt.title("Residuals Distribution")
plt.xlabel("Residual (Actual - Predicted)")
plt.show()"""),

    md("""## 8. Conclusions

1. Which model performed best? (Compare RMSE, MAE, R2)
2. Which features are most correlated with house value?
3. Are there patterns in the residuals?
4. What would you try next? (e.g., feature engineering, scaling, different models)"""),

    code("""print("House price project complete!")"""),
]


if __name__ == "__main__":
    write_notebook("Day1_Python_Pandas.ipynb", day1_cells)
    write_notebook("Day2_EDA_Visualization_Statistics.ipynb", day2_cells)
    write_notebook("Day3_Machine_Learning.ipynb", day3_cells)
    write_notebook("Capstone_Titanic.ipynb", titanic_cells)
    write_notebook("Capstone_Iris.ipynb", iris_cells)
    write_notebook("Capstone_House_Prices.ipynb", house_cells)
    print("\nAll notebooks generated successfully.")
