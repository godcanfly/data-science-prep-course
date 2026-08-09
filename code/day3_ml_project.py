"""
Day 3: Machine Learning + Capstone Live Coding Script
=====================================================
This is a clean Python script version of the Day 3 live coding.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)


# ============================================================
# 1. Prepare Features and Target
# ============================================================

features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

print("Features:")
print(X.head())
print("\nTarget:")
print(y.head())


# ============================================================
# 2. Preprocess Data
# ============================================================

# Fill missing Age values
X["Age"] = X["Age"].fillna(X["Age"].median())

# Convert Sex to numbers
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})

print(X.head())
print("\nMissing values:")
print(X.isnull().sum())


# ============================================================
# 3. Train/Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training set size:", X_train.shape[0])
print("Test set size:", X_test.shape[0])


# ============================================================
# 4. Train a Logistic Regression Model
# ============================================================

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("Model trained!")


# ============================================================
# 5. Make Predictions
# ============================================================

predictions = model.predict(X_test)
print("First 10 predictions:", predictions[:10])
print("First 10 actual:    ", y_test.values[:10])


# ============================================================
# 6. Evaluate the Model
# ============================================================

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# ============================================================
# 7. Feature Importance
# ============================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values("Coefficient", ascending=False)

print(importance)


# ============================================================
# 8. Visualize Feature Importance
# ============================================================

plt.figure(figsize=(8, 5))
sns.barplot(data=importance, x="Coefficient", y="Feature")
plt.title("Feature Importance")
plt.axvline(x=0, color="black", linestyle="--", linewidth=0.8)
plt.show()


# ============================================================
# 9. Try a Decision Tree (Optional)
# ============================================================

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
tree_predictions = tree.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_predictions)
print(f"Decision Tree Accuracy: {tree_accuracy:.2%}")


# ============================================================
# 10. Make a Prediction for a New Passenger
# ============================================================

new_passenger = pd.DataFrame({
    "Pclass": [1],
    "Sex": [1],
    "Age": [25],
    "Fare": [100]
})

prediction = model.predict(new_passenger)
probability = model.predict_proba(new_passenger)

print(f"Predicted survival: {prediction[0]}")
print(f"Probability of survival: {probability[0][1]:.2%}")
