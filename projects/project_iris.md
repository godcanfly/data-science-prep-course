# Capstone Project: Iris Flower Classification

## Goal
Build a model that predicts the species of an iris flower based on its measurements.

## Dataset
Iris dataset, available through scikit-learn or Seaborn.

## Step 1: Load and Explore

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load from seaborn
df = sns.load_dataset("iris")

print(df.shape)
df.head()
df.info()
df.describe()
```

## Step 2: EDA with Visualizations

```python
# Species counts
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="species")
plt.title("Count of Each Species")
plt.show()

# Pairplot
plt.figure(figsize=(10, 8))
sns.pairplot(df, hue="species")
plt.show()

# Boxplot of petal length by species
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="species", y="petal_length")
plt.title("Petal Length by Species")
plt.show()
```

## Step 3: Prepare Features

```python
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]
```

## Step 4: Train/Test Split

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## Step 5: Train Model

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

## Step 6: Evaluate

```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))
```

## Step 7: Predict on New Flower

```python
new_flower = pd.DataFrame({
    "sepal_length": [5.1],
    "sepal_width": [3.5],
    "petal_length": [1.4],
    "petal_width": [0.2]
})

prediction = model.predict(new_flower)
print("Predicted species:", prediction[0])
```

## Step 8: Conclusions

- Which features best separate the species?
- How accurate was your model?
- Why is this dataset considered a classic ML example?

## Extension Ideas
- Try K-Nearest Neighbors (KNN)
- Try a Decision Tree
- Visualize the decision boundary (advanced)
