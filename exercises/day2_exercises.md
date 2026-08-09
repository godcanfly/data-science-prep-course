# Day 2 Exercises: EDA + Visualization + Statistics

## Exercise 1: Quick EDA (10 minutes)

Load the Titanic dataset:

```python
import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)
```

Answer these questions with code:
1. How many missing values are in each column?
2. What percentage of the `Cabin` column is missing?
3. How many unique values are in the `Embarked` column?
4. What are the three most common embarkation ports?

---

## Exercise 2: Descriptive Statistics (10 minutes)

Compute the following for the `Fare` column:
1. Mean
2. Median
3. Standard deviation
4. Minimum and maximum

Which is larger, the mean or the median? What does that tell you about the distribution?

---

## Exercise 3: Conditional Probability (10 minutes)

Using the Titanic dataset, compute:
1. The survival rate for passengers in first class
2. The survival rate for passengers in third class
3. The survival rate for females under 18

---

## Exercise 4: Matplotlib Practice (15 minutes)

Create the following charts using Matplotlib:
1. A bar chart showing the number of passengers in each class
2. A histogram of passenger fares (use 30 bins)
3. A scatter plot of `Age` vs `Fare`, colored by survival status

Customize each chart with a title and axis labels.

---

## Exercise 5: Seaborn Practice (15 minutes)

Create the following charts using Seaborn:
1. A count plot of `Pclass`, separated by `Sex`
2. A boxplot of `Fare` by `Survived`
3. A histogram of `Age` with a KDE curve

---

## Exercise 6: Correlation (10 minutes)

1. Create a correlation matrix using these columns: `Age`, `Fare`, `Pclass`, `SibSp`, `Parch`, `Survived`
2. Display it as a heatmap with annotations
3. Which two variables have the strongest correlation?

---

## Exercise 7: Build a Mini EDA Report (30 minutes)

Create a new Colab notebook and write an EDA report with:
- A title and one-paragraph introduction
- Data overview (shape, missing values, summary statistics)
- At least 3 visualizations
- 3–5 bullet points of key findings

---

## Bonus Challenge

Investigate whether family size affects survival rate. Create a `FamilySize` column and plot survival rate by family size.
