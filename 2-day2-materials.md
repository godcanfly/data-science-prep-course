# Day 2 — EDA + Visualization + Statistics

## Learning Objectives

By the end of Day 2, the student will be able to:
- Perform exploratory data analysis using Pandas
- Compute and interpret descriptive statistics
- Understand correlation and basic probability
- Create common charts with Matplotlib and Seaborn
- Combine statistics and visualization into a short EDA report
- Explain findings in plain language

---

## Day 2 Schedule

| Time | Topic | Format |
|------|-------|--------|
| 09:00–09:30 | Recap Day 1 + quiz | Discussion |
| 09:30–10:30 | Exploratory Data Analysis | Live coding |
| 10:30–10:45 | Break | |
| 10:45–12:00 | Statistics for data science | Lecture + code |
| 12:00–13:00 | Lunch | |
| 13:00–14:00 | Matplotlib fundamentals | Live coding |
| 14:00–14:45 | Seaborn for better charts | Live coding |
| 14:45–15:00 | Break | |
| 15:00–16:30 | Build an EDA report | Project work |
| 16:30–17:00 | Present findings | 2-min talks |

---

## Part 1 — Recap (09:00–09:30)

### Quick Quiz
1. How do you read a CSV file with Pandas?
2. How do you select only rows where `Age > 30`?
3. What does `df.groupby("Sex")["Survived"].mean()` compute?
4. How do you save a DataFrame to CSV?

### Review Exercise (5 minutes)
Load the cleaned Titanic dataset and print the first 10 rows.

```python
import pandas as pd
df = pd.read_csv("cleaned_titanic.csv")
df.head(10)
```

---

## Part 2 — Exploratory Data Analysis (09:30–10:30)

### Slides / Talking Points

**Slide 1: What is EDA?**
- EDA = Exploratory Data Analysis
- Goal: understand the data before building models
- Ask questions, look for patterns, find problems

**Slide 2: The EDA Mindset**
1. What is the shape of the data?
2. What does each column mean?
3. Are there missing values?
4. What are the distributions?
5. Are there relationships between variables?

**Slide 3: Quick Overview**

```python
df.shape
 df.columns
 df.info()
 df.describe()
```

**Slide 4: Value Counts**

```python
 df["Sex"].value_counts()
 df["Pclass"].value_counts()
 df["Embarked"].value_counts()
```

**Slide 5: Detecting Missing Data**

```python
 df.isnull().sum()
 df.isnull().sum() / len(df) * 100  # percentage missing
```

**Slide 6: Unique Values**

```python
 df["Pclass"].nunique()
 df["Pclass"].unique()
```

---

## Part 3 — Statistics for Data Science (10:45–12:00)

### Slides / Talking Points

**Slide 7: Descriptive Statistics**

```python
 df["Age"].mean()
 df["Age"].median()
 df["Age"].std()     # standard deviation
 df["Age"].min()
 df["Age"].max()
```

- Mean: average
- Median: middle value (less affected by outliers)
- Standard deviation: how spread out the data is

**Slide 8: Distribution**
- A distribution shows how often each value appears
- Normal distribution = bell curve
- Many real-world things are approximately normal

**Slide 9: Outliers**
- Values much higher or lower than most of the data
- Can affect mean and machine learning models
- Boxplots help detect outliers

**Slide 10: Correlation**
- Correlation measures how two variables move together
- Range: -1 to +1
- +1 = strong positive relationship
- -1 = strong negative relationship
- 0 = no linear relationship

```python
 df[["Age", "Fare", "Survived"]].corr()
```

**Slide 11: Correlation is Not Causation**
- Ice cream sales correlate with drowning accidents
- Why? Both go up in summer
- Always ask: is there a third factor?

**Slide 12: Probability Basics**
- Probability = chance of an event
- Range: 0 (impossible) to 1 (certain)
- Example: P(survived | female) = survival rate among females

```python
# Survival probability
 df["Survived"].mean()

# Conditional probability
 df[df["Sex"] == "female"]["Survived"].mean()
 df[df["Sex"] == "male"]["Survived"].mean()
```

---

## Part 4 — Matplotlib (13:00–14:00)

### Slides / Talking Points

**Slide 13: Why Visualize?**
- Charts reveal patterns that tables hide
- Easier to communicate findings
- Essential for presentations and reports

**Slide 14: Importing Matplotlib**

```python
import matplotlib.pyplot as plt

# This line makes charts appear in Colab
%matplotlib inline
```

**Slide 15: Line Plot**

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

**Slide 16: Bar Chart**

```python
survival_counts = df["Survived"].value_counts()
plt.bar(["Died", "Survived"], survival_counts)
plt.title("Survival Counts")
plt.ylabel("Number of passengers")
plt.show()
```

**Slide 17: Histogram**

```python
plt.hist(df["Age"], bins=20, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
```

**Slide 18: Scatter Plot**

```python
plt.scatter(df["Age"], df["Fare"], alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
```

---

## Part 5 — Seaborn (14:00–14:45)

### Slides / Talking Points

**Slide 19: Why Seaborn?**
- Prettier charts with less code
- Built on top of Matplotlib
- Great for statistical plots

```python
import seaborn as sns
```

**Slide 20: Count Plot**

```python
sns.countplot(data=df, x="Sex")
plt.title("Count by Sex")
plt.show()
```

**Slide 21: Boxplot**

```python
sns.boxplot(data=df, x="Pclass", y="Age")
plt.title("Age Distribution by Class")
plt.show()
```

**Slide 22: Histogram with KDE**

```python
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution")
plt.show()
```

**Slide 23: Correlation Heatmap**

```python
corr = df[["Age", "Fare", "Pclass", "Survived", "FamilySize"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
```

**Slide 24: Pairplot**

```python
sns.pairplot(df[["Age", "Fare", "Survived"]], hue="Survived")
plt.show()
```

---

## Part 6 — EDA Report Project (15:00–16:30)

### Instructions for Students

Create a notebook called `Day2_EDA_Report` with the following sections:

#### Section 1: Introduction
- What dataset are you using?
- What question are you trying to answer?

#### Section 2: Data Overview
- Shape, columns, missing values
- Summary statistics

#### Section 3: Univariate Analysis
- 2 histograms or bar charts of single variables
- Explain what you see

#### Section 4: Bivariate Analysis
- 2 charts comparing two variables
- Examples: Age vs Fare, Survival by Sex, Fare by Class

#### Section 5: Correlation
- A correlation heatmap
- Interpret one strong correlation

#### Section 6: Conclusions
- 3–5 bullet points summarizing key findings

---

## Part 7 — Presentations (16:30–17:00)

Each student presents for 2 minutes:
1. What dataset did you use?
2. What was the most interesting finding?
3. Show your favorite chart and explain it

---

## Day 2 Live Coding Script

```python
# =====================================
# Day 2: EDA + Visualization Live Coding
# =====================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
 df = pd.read_csv(url)

# Basic EDA
 df.shape
 df.columns
 df.describe()
 df.isnull().sum()

# Value counts
 df["Sex"].value_counts()
 df["Pclass"].value_counts()

# Statistics
 df["Age"].mean()
 df["Age"].median()
 df["Age"].std()

# Conditional probability
 df[df["Sex"] == "female"]["Survived"].mean()
 df[df["Sex"] == "male"]["Survived"].mean()

# Correlation
 df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
 corr = df[["Age", "Fare", "Pclass", "Survived", "FamilySize"]].corr()

# Visualization
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived")
plt.title("Survival Counts")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Pclass", y="Age")
plt.title("Age by Passenger Class")
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
```

---

## Homework

1. Add 2 more charts to your EDA report
2. Write a one-paragraph summary of your findings
3. Read the Matplotlib and Seaborn cheatsheets

---

## Instructor Tips

- Encourage students to customize colors, titles, and labels
- Teach them to resize charts with `plt.figure(figsize=(width, height))`
- When students ask “which chart should I use?”, give a decision framework:
  - One numeric variable → histogram
  - One categorical variable → bar chart
  - Numeric vs categorical → boxplot
  - Numeric vs numeric → scatter plot
- Praise clear explanations more than pretty charts
