"""
Day 3 Exercise Solutions
=========================
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Exercise 2: Train/Test Split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Exercise 3 & 4: Build and evaluate model
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

X["Age"] = X["Age"].fillna(X["Age"].median())
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Exercise 5: Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values("Coefficient", ascending=False)

print("\nFeature Importance:")
print(importance)

# Exercise 6: Decision Tree
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
tree_predictions = tree.predict(X_test)
print("\nDecision Tree Accuracy:", accuracy_score(y_test, tree_predictions))

# Bonus: Adding Embarked feature
X_bonus = df[["Pclass", "Sex", "Age", "Fare", "Embarked"]].copy()
X_bonus["Age"] = X_bonus["Age"].fillna(X_bonus["Age"].median())
X_bonus["Sex"] = X_bonus["Sex"].map({"male": 0, "female": 1})
X_bonus["Embarked"] = X_bonus["Embarked"].fillna("S")
X_bonus = pd.get_dummies(X_bonus, columns=["Embarked"], drop_first=True)

X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(
    X_bonus, y, test_size=0.2, random_state=42
)

model_b = LogisticRegression(max_iter=1000)
model_b.fit(X_train_b, y_train_b)
predictions_b = model_b.predict(X_test_b)
print("\nBonus Model Accuracy (with Embarked):", accuracy_score(y_test_b, predictions_b))
