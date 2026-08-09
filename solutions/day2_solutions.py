"""
Day 2 Exercise Solutions
========================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# Exercise 1: Quick EDA
print("Missing values per column:")
print(df.isnull().sum())

print("\nCabin missing percentage:")
print(f"{df['Cabin'].isnull().sum() / len(df) * 100:.1f}%")

print("\nUnique embarked values:", df["Embarked"].nunique())
print("\nTop embarkation ports:")
print(df["Embarked"].value_counts())

# Exercise 2: Descriptive statistics
print("\nFare mean:", df["Fare"].mean())
print("Fare median:", df["Fare"].median())
print("Fare std:", df["Fare"].std())
print("Fare min:", df["Fare"].min())
print("Fare max:", df["Fare"].max())

# Exercise 3: Conditional probability
print("\nFirst class survival rate:", df[df["Pclass"] == 1]["Survived"].mean())
print("Third class survival rate:", df[df["Pclass"] == 3]["Survived"].mean())
female_children = df[(df["Sex"] == "female") & (df["Age"] < 18)]
print("Female under 18 survival rate:", female_children["Survived"].mean())

# Exercise 4: Matplotlib
plt.figure(figsize=(6, 4))
class_counts = df["Pclass"].value_counts().sort_index()
plt.bar(class_counts.index, class_counts.values)
plt.title("Number of Passengers by Class")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Fare"], bins=30, edgecolor="black")
plt.title("Distribution of Fares")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 5))
for survived, color in [(0, "red"), (1, "green")]:
    subset = df[df["Survived"] == survived]
    plt.scatter(subset["Age"], subset["Fare"], alpha=0.5, label=f"Survived={survived}", color=color)
plt.title("Age vs Fare by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend()
plt.show()

# Exercise 5: Seaborn
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Pclass", hue="Sex")
plt.title("Passenger Count by Class and Sex")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Survived", y="Fare")
plt.title("Fare by Survival Status")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution")
plt.show()

# Exercise 6: Correlation heatmap
numeric_cols = ["Age", "Fare", "Pclass", "SibSp", "Parch", "Survived"]
corr = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Bonus: Family size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
survival_by_family = df.groupby("FamilySize")["Survived"].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(data=survival_by_family, x="FamilySize", y="Survived")
plt.title("Survival Rate by Family Size")
plt.ylabel("Survival Rate")
plt.show()
