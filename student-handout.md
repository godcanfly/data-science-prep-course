# Student Handout: 3-Day Data Science Prep Course

## Welcome!

This handout is your quick reference for the 3-day intensive. Keep it open while you code.

---

## Before You Start

1. Open Google Colab: [colab.research.google.com](https://colab.research.google.com)
2. Create a new notebook for each day
3. Sign up for GitHub: [github.com](https://github.com)
4. Save your notebooks often

---

## Day 1 Checklist

- [ ] I can create variables and use different data types
- [ ] I can use lists, dictionaries, loops, and functions
- [ ] I can load a CSV file with Pandas
- [ ] I can inspect a DataFrame with `.head()`, `.info()`, `.describe()`
- [ ] I can filter rows and select columns
- [ ] I can group data and compute aggregates
- [ ] I can save a cleaned CSV file

### Day 1 Key Commands

```python
import pandas as pd

df = pd.read_csv("file.csv")
df.head()
df.shape
df.columns
df.describe()
df.info()
df["column"]
df[["col1", "col2"]]
df[df["age"] > 30]
df.sort_values("age", ascending=False)
df.groupby("category")["value"].mean()
df["new_col"] = df["col1"] + df["col2"]
df.to_csv("output.csv", index=False)
```

---

## Day 2 Checklist

- [ ] I can compute mean, median, and standard deviation
- [ ] I understand what correlation means
- [ ] I can create histograms, bar charts, and scatter plots
- [ ] I can use Seaborn for better-looking charts
- [ ] I can build a simple EDA report

### Day 2 Key Commands

```python
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# Statistics
df["col"].mean()
df["col"].median()
df["col"].std()
df[["col1", "col2"]].corr()

# Matplotlib
plt.plot(x, y)
plt.bar(x, y)
plt.hist(data, bins=20)
plt.scatter(x, y)
plt.title("Title")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

# Seaborn
sns.countplot(data=df, x="col")
sns.boxplot(data=df, x="cat", y="num")
sns.histplot(data=df, x="num", kde=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
```

---

## Day 3 Checklist

- [ ] I can explain supervised vs unsupervised learning
- [ ] I can split data into training and testing sets
- [ ] I can train a classification model
- [ ] I can evaluate a model with accuracy and confusion matrix
- [ ] I can upload a project to GitHub

### Day 3 Key Commands

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(confusion_matrix(y_test, predictions))
```

---

## Chart Choice Guide

| Question | Chart |
|---|---|
| How is one numeric variable distributed? | Histogram |
| How often does each category appear? | Bar chart / count plot |
| How does a numeric variable differ by category? | Box plot |
| Is there a relationship between two numeric variables? | Scatter plot |
| How correlated are several numeric variables? | Heatmap |

---

## Debugging Tips

1. Read the error message carefully — usually the last line tells you what is wrong
2. Check that variable names are spelled correctly
3. Check that parentheses and brackets are closed
4. Use `print()` to see what your variables contain
5. When stuck, try the simplest possible version first
6. Google the error message — someone else has had the same problem

---

## Useful Websites

| Resource | URL | Use |
|---|---|---|
| Google Colab | colab.research.google.com | Run Python notebooks |
| Kaggle | kaggle.com | Datasets and competitions |
| Pandas Docs | pandas.pydata.org/docs | Pandas reference |
| scikit-learn Docs | scikit-learn.org | Machine learning reference |
| Stack Overflow | stackoverflow.com | Q&A for coding problems |
| StatQuest | youtube.com/@statquest | Statistics explained simply |

---

## 30-Day Post-Course Plan

| Week | Action |
|---|---|
| Week 1 | Rebuild all 3 daily notebooks from scratch |
| Week 2 | Complete 2 Kaggle "Getting Started" competitions |
| Week 3 | Learn Git and upload 3 projects to GitHub |
| Week 4 | Read one data science case study or watch one lecture per day |

---

## Project Presentation Template

Use this structure for your 3-minute presentation:

1. **Problem**: What question are you trying to answer?
2. **Data**: What dataset did you use?
3. **Analysis**: What did you discover in EDA?
4. **Model**: What model did you build?
5. **Results**: What was your accuracy or key metric?
6. **Next Steps**: What would you improve?

---

## Final Reminder

> Data science is not about memorizing code. It is about asking good questions, cleaning messy data, and explaining your findings clearly. You have already started.
