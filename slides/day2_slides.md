# Day 2 Slides Outline

## Slide 1: What is EDA?
- Exploratory Data Analysis
- Understand the data before building models
- Ask questions, look for patterns, find problems

## Slide 2: The EDA Mindset
- What is the shape?
- What does each column mean?
- Are there missing values?
- What are the distributions?
- Are there relationships?

## Slide 3: Quick Overview
```python
df.shape
df.columns
df.info()
df.describe()
```

## Slide 4: Value Counts
```python
df["Sex"].value_counts()
df["Pclass"].value_counts()
```

## Slide 5: Detecting Missing Data
```python
df.isnull().sum()
```

## Slide 6: Descriptive Statistics
- Mean, median, std, min, max

## Slide 7: Distribution
- How often each value appears
- Normal distribution = bell curve

## Slide 8: Outliers
- Values much higher or lower than most data
- Affect mean and models
- Boxplots help detect

## Slide 9: Correlation
- Measures how two variables move together
- Range: -1 to +1

## Slide 10: Correlation is Not Causation
- Example: ice cream and drowning
- Ask: is there a third factor?

## Slide 11: Probability Basics
- Chance of an event
- Conditional probability

## Slide 12: Why Visualize?
- Reveal hidden patterns
- Communicate findings
- Essential for presentations

## Slide 13: Importing Matplotlib
```python
import matplotlib.pyplot as plt
%matplotlib inline
```

## Slide 14: Line Plot
```python
plt.plot(x, y)
plt.title("...")
plt.show()
```

## Slide 15: Bar Chart
```python
plt.bar(x, y)
```

## Slide 16: Histogram
```python
plt.hist(data, bins=20)
```

## Slide 17: Scatter Plot
```python
plt.scatter(x, y, alpha=0.5)
```

## Slide 18: Why Seaborn?
- Prettier charts
- Less code
- Statistical plots

## Slide 19: Count Plot
```python
sns.countplot(data=df, x="Sex")
```

## Slide 20: Boxplot
```python
sns.boxplot(data=df, x="Pclass", y="Age")
```

## Slide 21: Histogram with KDE
```python
sns.histplot(data=df, x="Age", kde=True)
```

## Slide 22: Correlation Heatmap
```python
sns.heatmap(corr, annot=True, cmap="coolwarm")
```

## Slide 23: EDA Report Project
- Introduction
- Data overview
- Univariate analysis
- Bivariate analysis
- Correlation
- Conclusions

## Slide 24: Presentation Tips
- Explain charts simply
- Focus on the most interesting finding
- Use titles and labels

## Slide 25: What We Learned Today
- EDA workflow
- Descriptive statistics
- Probability and correlation
- Matplotlib and Seaborn

## Slide 26: Homework
- Add 2 more charts
- Write a one-paragraph summary
- Read Matplotlib and Seaborn cheatsheets

## Slide 27: Tomorrow Preview
- Machine Learning
- Train/test split
- First classification model
