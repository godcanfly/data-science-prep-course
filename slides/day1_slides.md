# Day 1 Slides Outline

## Slide 1: Welcome
- 3-day intensive for university data science prep
- Goal: confidence + portfolio project
- Rule: type every line of code yourself

## Slide 2: Tools We Will Use
- Google Colab: free Python notebooks in the browser
- Python: the main language of data science
- Pandas: Excel-like tables in Python

## Slide 3: Open Your First Colab Notebook
1. Go to `colab.research.google.com`
2. Click **File → New notebook**
3. Rename it to `Day1_Python_Pandas`
4. Type: `print("Hello, Data Science!")`
5. Press `Shift + Enter`

## Slide 4: Why Python?
- Easy to read
- Huge community
- Thousands of libraries for AI and data
- Used in every university data science program

## Slide 5: Variables
- A variable is a labeled box that stores a value
- Python figures out the type automatically

## Slide 6: Data Types
- `str`, `int`, `float`, `bool`

## Slide 7: Lists
- Ordered collection of items
- Indexing, append, length

## Slide 8: Dictionaries
- Key-value pairs
- Like a real dictionary

## Slide 9: Conditions
- `if`, `elif`, `else`

## Slide 10: Loops
- `for` and `while`

## Slide 11: Functions
- Reusable blocks of code
- Take inputs, return outputs

## Slide 12: String Formatting
- f-strings: `f"{name} is {age} years old"`

## Slide 13: What is Pandas?
- Python library for data tables
- Like Excel but with code
- Industry standard

## Slide 14: Importing Pandas
```python
import pandas as pd
```

## Slide 15: Reading a CSV
```python
df = pd.read_csv(url)
```

## Slide 16: Inspecting a DataFrame
- `.head()`, `.tail()`, `.shape`, `.columns`, `.info()`, `.describe()`

## Slide 17: Series vs DataFrame
- Series = one column
- DataFrame = table

## Slide 18: Selecting Columns
```python
df["Name"]
df[["Name", "Age"]]
```

## Slide 19: Selecting Rows by Position
```python
df.iloc[0]
df.iloc[0:5]
```

## Slide 20: Filtering
```python
df[df["Age"] > 30]
df[(df["Sex"] == "female") & (df["Fare"] > 50)]
```

## Slide 21: Sorting
```python
df.sort_values("Age", ascending=False)
```

## Slide 22: Adding New Columns
```python
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
```

## Slide 23: Dropping Columns
```python
df = df.drop(columns=["Cabin"])
```

## Slide 24: Handling Missing Values
```python
df.isnull().sum()
df["Age"] = df["Age"].fillna(df["Age"].median())
```

## Slide 25: Groupby
```python
df.groupby("Sex")["Survived"].mean()
```

## Slide 26: Saving Data
```python
df.to_csv("cleaned_titanic.csv", index=False)
```

## Slide 27: What We Learned Today
- Python basics
- Pandas DataFrames
- Loading, filtering, transforming, grouping data
- Saving cleaned data

## Slide 28: Homework
- Rebuild today’s notebook from scratch
- Try grouping by two columns
- Read Pandas cheatsheet

## Slide 29: Tomorrow Preview
- Exploratory Data Analysis
- Charts with Matplotlib and Seaborn
- Basic statistics
