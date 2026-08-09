"""
Day 1: Python + Pandas Live Coding Script
=========================================
This is a clean Python script version of the Day 1 live coding.
To run in Google Colab or Jupyter Notebook, copy each section into its own cell.
"""

# ============================================================
# 1. Python Basics
# ============================================================

# First line of Python
print("Hello, Data Science!")

# Variables
name = "Alice"
age = 18
height = 1.65
is_student = True
print(name, age, height, is_student)

# Check types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Lists
scores = [85, 90, 78, 92]
print(scores[0])     # First item
print(scores[-1])    # Last item
print(len(scores))   # Number of items
scores.append(88)
print(scores)

# Loops
for s in scores:
    print(s)

# Functions
def average(numbers):
    return sum(numbers) / len(numbers)

print(average(scores))

# String formatting
print(f"{name} is {age} years old.")

# Dictionaries
student = {
    "name": "Alice",
    "age": 18,
    "major": "Data Science"
}
print(student["name"])
student["gpa"] = 3.8
print(student)


# ============================================================
# 2. Introduction to Pandas
# ============================================================

import pandas as pd

# Load data from a URL
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# Inspect the data
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns.tolist())
print(df.info())
print(df.describe())


# ============================================================
# 3. Selecting and Filtering
# ============================================================

# Select one column
print(df["Name"].head())

# Select multiple columns
print(df[["Name", "Age", "Sex", "Survived"]].head())

# Select rows by position
print(df.iloc[0])
print(df.iloc[0:5])

# Filter by condition
print(df[df["Age"] > 30].head())

# Filter by category
print(df[df["Sex"] == "female"].head())

# Multiple conditions
print(df[(df["Sex"] == "female") & (df["Fare"] > 50)].head())

# Sort values
print(df.sort_values("Age", ascending=False).head())


# ============================================================
# 4. Transformations
# ============================================================

# Add a new column
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print(df[["SibSp", "Parch", "FamilySize"]].head())

# Check missing values
print(df.isnull().sum())

# Fill missing Age values with the median
df["Age"] = df["Age"].fillna(df["Age"].median())
print(df.isnull().sum())


# ============================================================
# 5. Groupby and Aggregation
# ============================================================

# Average survival rate by sex
print(df.groupby("Sex")["Survived"].mean())

# Multiple aggregations by passenger class
print(df.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "mean",
    "Survived": "mean"
}))


# ============================================================
# 6. Save Cleaned Data
# ============================================================

df.to_csv("cleaned_titanic.csv", index=False)
print("File saved!")
