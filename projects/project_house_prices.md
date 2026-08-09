# Capstone Project: California House Price Prediction

## Goal
Build a regression model that predicts the median house value based on location and neighborhood features.

## Dataset
California Housing dataset from scikit-learn.

## Step 1: Load and Explore

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
df = housing.frame

print(df.shape)
df.head()
df.info()
df.describe()
```

## Step 2: EDA with Visualizations

```python
# Distribution of house prices
plt.figure(figsize=(8, 5))
sns.histplot(df["MedHouseVal"], kde=True, bins=50)
plt.title("Distribution of Median House Values")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()

# Scatter: income vs house value
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="MedInc", y="MedHouseVal", alpha=0.3)
plt.title("Median Income vs House Value")
plt.show()
```

## Step 3: Prepare Features

```python
X = df.drop(columns=["MedHouseVal"])
y = df["MedHouseVal"]
```

## Step 4: Train/Test Split

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## Step 5: Train a Regression Model

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, predictions))
print("MAE:", mean_absolute_error(y_test, predictions))
```

## Step 6: Visualize Predictions

```python
plt.figure(figsize=(8, 5))
plt.scatter(y_test, predictions, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted House Values")
plt.show()
```

## Step 7: Conclusions

- Which features are most correlated with house value?
- How well did your model perform?
- Why might the model struggle with very high house values?

## Extension Ideas
- Try a Decision Tree Regressor
- Try a Random Forest Regressor
- Remove the cap at $500,000 and see how the model changes
