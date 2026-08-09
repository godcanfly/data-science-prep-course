"""
Day 2: EDA + Visualization + Statistics Live Coding Script
==========================================================
This is a clean Python script version of the Day 2 live coding.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# ============================================================
# 1. Exploratory Data Analysis
# ============================================================

# Basic shape and structure
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(10))
print(df.info())
print(df.describe())

# Value counts for categorical columns
print(df["Sex"].value_counts())
print(df["Pclass"].value_counts())
print(df["Embarked"].value_counts())

# Missing values
print(df.isnull().sum())
print("\nPercentage missing:")
print((df.isnull().sum() / len(df) * 100).round(2))


# ============================================================
# 2. Statistics
# ============================================================

# Descriptive statistics for Age
print("Mean:", df["Age"].mean())
print("Median:", df["Age"].median())
print("Std:", df["Age"].std())
print("Min:", df["Age"].min())
print("Max:", df["Age"].max())

# Conditional probabilities
print("Overall survival rate:", df["Survived"].mean())
print("Female survival rate:", df[df["Sex"] == "female"]["Survived"].mean())
print("Male survival rate:", df[df["Sex"] == "male"]["Survived"].mean())

# Correlation
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
corr = df[["Age", "Fare", "Pclass", "Survived", "FamilySize"]].corr()
print(corr)


# ============================================================
# 3. Matplotlib Charts
# ============================================================

# Bar chart of survival
survival_counts = df["Survived"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(["Died", "Survived"], survival_counts, color=["salmon", "lightgreen"])
plt.title("Survival Counts")
plt.ylabel("Number of passengers")
plt.show()

# Histogram of ages
plt.figure(figsize=(8, 5))
plt.hist(df["Age"].dropna(), bins=20, edgecolor="black", color="skyblue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Scatter plot: Age vs Fare
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Fare"], alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()


# ============================================================
# 4. Seaborn Charts
# ============================================================

# Count plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex")
plt.title("Count by Sex")
plt.show()

# Boxplot: Age by class
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Pclass", y="Age")
plt.title("Age Distribution by Passenger Class")
plt.show()

# Histogram with KDE
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution with KDE")
plt.show()

# Survival by sex
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Sex")
plt.ylabel("Survival Rate")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Matrix")
plt.show()


# ============================================================
# 5. Mini EDA Report
# ============================================================

print("=== MINI EDA REPORT ===")
print(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
print(f"Average age: {df['Age'].mean():.1f}")
print(f"Overall survival rate: {df['Survived'].mean():.1%}")
print(f"Female survival rate: {df[df['Sex'] == 'female']['Survived'].mean():.1%}")
print(f"Male survival rate: {df[df['Sex'] == 'male']['Survived'].mean():.1%}")
print("\nKey insight: Female passengers had a much higher survival rate than male passengers.")
