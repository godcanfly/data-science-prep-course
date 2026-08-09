"""
Day 1 Exercise Solutions
======================
"""

import pandas as pd

# Exercise 1: Variables
name = "Alice"
age = 18
height = 1.65
likes_data_science = True

print(name, age, height, likes_data_science)

# Exercise 2: List Operations
scores = [72, 88, 91, 67, 95, 83]
print("First score:", scores[0])
print("Last score:", scores[-1])
scores.append(78)
print("Total scores:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))

# Exercise 3: Loops with bonus
for s in scores:
    print(s * 1.05)

# Exercise 4: Function
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", calculate_average(scores))

# Exercise 5: Dictionary
movie = {
    "title": "Inception",
    "year": 2010,
    "director": "Christopher Nolan",
    "rating": 8.8
}
print(movie["title"])
movie["genre"] = "Sci-Fi"
print(movie)

# Exercise 6: Pandas basics
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(8))
print(df.describe())

# Exercise 7: Filtering
print("Female passengers:")
print(df[df["Sex"] == "female"].head())

print("\nHigh fare passengers:")
print(df[df["Fare"] > 50].head())

print("\nFirst class survivors:")
print(df[(df["Pclass"] == 1) & (df["Survived"] == 1)].head())

print("\nSorted by age:")
print(df.sort_values("Age", ascending=False).head())

# Exercise 8: Groupby
print("\nAverage age:", df["Age"].mean())
print("\nSurvival rate by class:")
print(df.groupby("Pclass")["Survived"].mean())
print("\nAverage fare by embarkation port:")
print(df.groupby("Embarked")["Fare"].mean())

# Bonus: AgeGroup
def classify_age(age):
    if pd.isnull(age):
        return "Unknown"
    elif age < 18:
        return "Child"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(classify_age)
print(df[["Age", "AgeGroup"]].head(10))
