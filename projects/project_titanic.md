# Capstone Project: Titanic Survival Prediction

## Goal
Build a model that predicts whether a passenger survived the Titanic shipwreck.

## Dataset
Titanic dataset from `https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv`

## Step 1: Load and Explore

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

print(df.shape)
df.head()
df.info()
df.describe()
```

## Step 2: Clean the Data

```python
# Fill missing Age values with median
 df["Age"] = df["Age"].fillna(df["Age"].median())

# Drop Cabin (too many missing values) or ignore it
 df = df.drop(columns=["Cabin"])

# Fill missing Embarked with mode
 df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
```

## Step 3: EDA with Visualizations

Create at least 3 charts:

```python
# Survival rate by sex
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Sex")
plt.show()

# Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", kde=True, bins=20)
plt.title("Age Distribution")
plt.show()

# Survival by class
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.show()
```

## Step 4: Prepare Features

```python
features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

X["Sex"] = X["Sex"].map({"male": 0, "female": 1})
```

## Step 5: Train/Test Split

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## Step 6: Train Model

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

## Step 7: Evaluate

```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))
```

## Step 8: Conclusions

Write 3–5 bullet points summarizing:
- What you learned about the data
- Which factors seemed most important
- How accurate your model was
- What you could improve next

## Extension Ideas
- Try a DecisionTreeClassifier
- Add more features (SibSp, Parch, Embarked)
- Engineer a new feature like `FamilySize`
- Use one-hot encoding for categorical variables
