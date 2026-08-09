# Day 1 — Python + Pandas

## Learning Objectives

By the end of Day 1, the student will be able to:
- Write basic Python: variables, lists, dictionaries, loops, functions
- Load a CSV file using Pandas
- Select, filter, sort, and group data
- Handle missing values and create new columns
- Save a cleaned dataset

---

## Day 1 Schedule

| Time | Topic | Format |
|------|-------|--------|
| 09:00–09:30 | Welcome + setup | Discussion |
| 09:30–10:30 | Python crash course | Live coding |
| 10:30–10:45 | Break | |
| 10:45–12:00 | Python exercises | Hands-on |
| 12:00–13:00 | Lunch | |
| 13:00–14:00 | Intro to Pandas | Live coding |
| 14:00–14:45 | Selecting & filtering | Hands-on |
| 14:45–15:00 | Break | |
| 15:00–16:30 | Transformations & aggregation | Hands-on |
| 16:30–17:00 | Wrap-up + homework | Review |

---

## Part 1 — Welcome & Setup (09:00–09:30)

### Slides / Talking Points

**Slide 1: Welcome**
- 3-day intensive for university data science prep
- Goal: confidence + portfolio project
- Rule: type every line of code yourself

**Slide 2: Tools We Will Use**
- Google Colab: free Python notebooks in the browser
- Python: the main language of data science
- Pandas: Excel-like tables in Python

**Slide 3: Open Your First Colab Notebook**
1. Go to `colab.research.google.com`
2. Click **File → New notebook**
3. Rename it to `Day1_Python_Pandas`
4. Type in a cell:
   ```python
   print("Hello, Data Science!")
   ```
5. Press `Shift + Enter` to run

**Slide 4: Why Python?**
- Easy to read
- Huge community
- Thousands of libraries for AI and data
- Used in every university data science program

---

## Part 2 — Python Crash Course (09:30–10:30)

### Slides / Talking Points

**Slide 5: Variables**
- A variable is a labeled box that stores a value
- Python figures out the type automatically

```python
name = "Alice"
age = 18
height = 1.65
is_student = True
```

**Slide 6: Data Types**

| Type | Example | Description |
|------|---------|-------------|
| `str` | `"hello"` | Text |
| `int` | `25` | Whole number |
| `float` | `3.14` | Decimal number |
| `bool` | `True` | True or False |

```python
type(name)  # <class 'str'>
type(age)   # <class 'int'>
```

**Slide 7: Lists**
- Ordered collection of items
- Can mix types (not recommended)

```python
scores = [85, 90, 78, 92]
scores[0]       # 85
scores[-1]      # 92
scores.append(88)
len(scores)     # 5
```

**Slide 8: Dictionaries**
- Store key-value pairs
- Like a real dictionary: word → definition

```python
student = {
    "name": "Alice",
    "age": 18,
    "major": "Data Science"
}
student["name"]        # Alice
student["gpa"] = 3.8
```

**Slide 9: Conditions**

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)
```

**Slide 10: Loops**

```python
# For loop
for s in scores:
    print(s)

# While loop
n = 0
while n < 5:
    print(n)
    n += 1
```

**Slide 11: Functions**
- Reusable blocks of code
- Take inputs, return outputs

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

**Slide 12: String Formatting**

```python
name = "Alice"
age = 18
print(f"{name} is {age} years old.")
```

---

## Part 3 — Python Exercises (10:45–12:00)

Give students these exercises. They should write code in new Colab cells.

### Exercise 1: Variables
Create variables for your name, age, and whether you like data science. Print them all.

### Exercise 2: List Operations
```python
prices = [12.5, 18.0, 7.5, 25.0, 10.0]
```
- Print the first price
- Print the last price
- Add a new price of 15.0
- Print the length of the list

### Exercise 3: Loop Practice
Print every price with a 10% discount applied.

### Exercise 4: Function Practice
Write a function `calculate_average(numbers)` that returns the average of a list.

### Exercise 5: Dictionary Practice
Create a dictionary for a book with keys: `title`, `author`, `year`. Print each value.

---

## Part 4 — Introduction to Pandas (13:00–14:00)

### Slides / Talking Points

**Slide 13: What is Pandas?**
- Python library for data tables
- Like Excel or Google Sheets, but with code
- Industry standard for data manipulation

**Slide 14: Importing Pandas**

```python
import pandas as pd
```

**Slide 15: Reading a CSV**

```python
# From a URL
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# From local file (after uploading to Colab)
# df = pd.read_csv("titanic.csv")
```

**Slide 16: Inspecting a DataFrame**

```python
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.shape         # (rows, columns)
df.columns       # Column names
df.info()        # Data types and missing values
df.describe()    # Summary statistics for numbers
```

**Slide 17: Series vs DataFrame**
- A `Series` is one column
- A `DataFrame` is a table of multiple columns

```python
df["Name"]           # Series
df[["Name", "Age"]]  # DataFrame (two columns)
```

---

## Part 5 — Selecting & Filtering (14:00–14:45)

### Slides / Talking Points

**Slide 18: Selecting Columns**

```python
df["Name"]
df[["Name", "Age", "Survived"]]
```

**Slide 19: Selecting Rows by Position**

```python
df.iloc[0]       # First row
df.iloc[0:5]     # First 5 rows
```

**Slide 20: Selecting Rows by Label/Condition**

```python
# Filter rows where Age > 30
older = df[df["Age"] > 30]

# Filter female passengers
female = df[df["Sex"] == "female"]

# Multiple conditions
rich_females = df[(df["Sex"] == "female") & (df["Fare"] > 50)]
```

**Slide 21: Sorting**

```python
df.sort_values("Age", ascending=False)
df.sort_values(["Pclass", "Age"])
```

---

## Part 6 — Transformations & Aggregation (15:00–16:30)

### Slides / Talking Points

**Slide 22: Adding New Columns**

```python
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
```

**Slide 23: Dropping Columns**

```python
df = df.drop(columns=["Cabin"])
```

**Slide 24: Handling Missing Values**

```python
df.isnull().sum()                # Count missing per column
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df.dropna()                 # Drop rows with any missing value
```

**Slide 25: Groupby**

```python
# Average age by passenger class
df.groupby("Pclass")["Age"].mean()

# Survival rate by sex
df.groupby("Sex")["Survived"].mean()

# Multiple aggregations
df.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "mean",
    "Survived": "mean"
})
```

**Slide 26: Saving Data**

```python
df.to_csv("cleaned_titanic.csv", index=False)
```

---

## Part 7 — Wrap-Up (16:30–17:00)

### Slides / Talking Points

**Slide 27: What We Learned Today**
- Python basics
- Pandas DataFrames
- Loading, filtering, transforming, grouping data
- Saving cleaned data

**Slide 28: Homework**
1. Rebuild today’s notebook from scratch (no copy-paste)
2. Try grouping by two columns: `df.groupby(["Sex", "Pclass"])["Survived"].mean()`
3. Read Pandas cheatsheet

**Slide 29: Tomorrow Preview**
- Exploratory Data Analysis
- Charts with Matplotlib and Seaborn
- Basic statistics

---

## Day 1 Live Coding Script

This is the full script the instructor should type live. Students follow along.

```python
# =====================================
# Day 1: Python + Pandas Live Coding
# =====================================

# --- Python basics ---
print("Hello, Data Science!")

name = "Alice"
age = 18
print(f"{name} is {age} years old.")

scores = [85, 90, 78, 92]
print(scores[0])
print(scores[-1])
scores.append(88)
print(len(scores))

for s in scores:
    print(s)

def average(numbers):
    return sum(numbers) / len(numbers)

print(average(scores))

# --- Pandas ---
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

df.head()
df.shape
df.columns
df.info()
df.describe()

# Select columns
df["Name"].head()
df[["Name", "Age", "Sex", "Survived"]].head()

# Filter
df[df["Age"] > 30].head()
df[df["Sex"] == "female"].head()

# Add column
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Missing values
df.isnull().sum()
df["Age"] = df["Age"].fillna(df["Age"].median())

# Groupby
df.groupby("Sex")["Survived"].mean()
df.groupby("Pclass").agg({"Age": "mean", "Fare": "mean", "Survived": "mean"})

# Save
df.to_csv("cleaned_titanic.csv", index=False)
```

---

## Instructor Tips

- Spend no more than 10 minutes on slides before live coding
- When students get errors, ask: “What does the error message say?”
- Show them how to use `?` in Colab, e.g. `df.groupby?`
- Emphasize that copying code is fine at this stage — understanding comes with repetition
