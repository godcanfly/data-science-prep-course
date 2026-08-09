# Day 3 — Machine Learning + Capstone Project

## Learning Objectives

By the end of Day 3, the student will be able to:
- Explain what machine learning is in plain language
- Distinguish supervised from unsupervised learning
- Split data into training and testing sets
- Build a classification model using scikit-learn
- Evaluate a model with accuracy and confusion matrix
- Complete an end-to-end data science project
- Present a project in 3 minutes
- Upload a project to GitHub

---

## Day 3 Schedule

| Time | Topic | Format |
|------|-------|--------|
| 09:00–09:30 | Recap Day 2 | Discussion |
| 09:30–10:30 | Machine learning concepts | Lecture |
| 10:30–10:45 | Break | |
| 10:45–12:00 | Build first ML model | Live coding |
| 12:00–13:00 | Lunch | |
| 13:00–14:00 | Model evaluation | Hands-on |
| 14:00–14:45 | Choose capstone project | Planning |
| 14:45–15:00 | Break | |
| 15:00–16:30 | Build capstone | Project work |
| 16:30–17:00 | Presentations + next steps | Demo + wrap-up |

---

## Part 1 — Recap Day 2 (09:00–09:30)

### Quick Quiz
1. What is the difference between a histogram and a bar chart?
2. What does correlation measure?
3. Name two Seaborn plots.
4. What should every chart have (title, labels, etc.)?

### Review Exercise (10 minutes)
Load the Titanic data and create:
- A count plot of `Pclass`
- A boxplot of `Fare` by `Survived`

---

## Part 2 — Machine Learning Concepts (09:30–10:30)

### Slides / Talking Points

**Slide 1: What is Machine Learning?**
- Traditional programming: human writes rules
- Machine learning: computer learns patterns from data
- Input data + answers → model → predictions on new data

**Slide 2: The ML Recipe**
1. Collect data
2. Prepare / clean data
3. Choose a model
4. Train the model on training data
5. Test the model on new data
6. Evaluate and improve

**Slide 3: Supervised Learning**
- We have labeled examples: input + correct answer
- Two main types:
  - Classification: predict a category (survived/died, spam/not spam)
  - Regression: predict a number (house price, temperature)

**Slide 4: Unsupervised Learning**
- We do not have labels
- The model finds patterns or groups
- Example: customer segmentation

**Slide 5: Features and Target**
- Features (X): input columns used for prediction
- Target (y): the value we want to predict
- In Titanic: features = Age, Sex, Fare, etc.; target = Survived

**Slide 6: Train/Test Split**
- We train on one part of the data
- We test on a separate part the model has never seen
- This checks if the model can generalize

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Slide 7: Overfitting vs Underfitting**
- Underfitting: model too simple, misses patterns
- Overfitting: model memorizes training data, fails on new data
- Goal: balance between the two

---

## Part 3 — First ML Model (10:45–12:00)

### Slides / Talking Points

**Slide 8: Prepare Data for ML**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# Select simple features
features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

# Handle missing values
X["Age"] = X["Age"].fillna(X["Age"].median())

# Convert text to numbers
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Slide 9: Train a Model**

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

**Slide 10: Make Predictions**

```python
predictions = model.predict(X_test)
print(predictions[:10])
```

---

## Part 4 — Model Evaluation (13:00–14:00)

### Slides / Talking Points

**Slide 11: Accuracy**

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
```

- Accuracy = percentage of correct predictions
- Easy to understand but can be misleading on imbalanced data

**Slide 12: Confusion Matrix**

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predictions)
print(cm)
```

| | Predicted Died | Predicted Survived |
|---|---|---|
| Actual Died | True Negative | False Positive |
| Actual Survived | False Negative | True Positive |

**Slide 13: Precision and Recall (Briefly)**

- Precision: of those predicted survived, how many actually survived?
- Recall: of those who actually survived, how many did we find?
- Useful for medical or safety problems

```python
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))
```

**Slide 14: Feature Importance**

```python
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})
print(importance)
```

---

## Part 5 — Choose Capstone Project (14:00–14:45)

### Project Options

Students choose one. Provide the corresponding project template from `projects/`.

#### Option A: Titanic Survival Prediction (Classification)
- Predict who survived the Titanic
- Good first ML project
- Dataset is small and well-known

#### Option B: Iris Flower Classification (Classification)
- Predict flower species from measurements
- Very clean dataset
- Great for understanding multi-class classification

#### Option C: House Price Prediction (Regression)
- Predict house prices from features
- More numbers, good for regression practice

### Capstone Requirements
1. Load and explore the data
2. Clean and prepare features
3. Create at least 3 visualizations
4. Build a machine learning model
5. Evaluate the model
6. Write conclusions
7. Save notebook and upload to GitHub

---

## Part 6 — Capstone Work Time (15:00–16:30)

### Student Work Plan

| Time | Task |
|------|------|
| 15:00–15:20 | Load data and do EDA |
| 15:20–15:50 | Clean data and prepare features |
| 15:50–16:10 | Build and train model |
| 16:10–16:25 | Evaluate and add visualizations |
| 16:25–16:30 | Finalize notebook |

### Instructor Role
- Walk around and answer questions
- Help with errors
- Encourage students to explain what they are doing
- Do not write code for them

---

## Part 7 — Presentations & Next Steps (16:30–17:00)

### Presentation Format (3 minutes each)
1. What problem did you solve?
2. What data did you use?
3. What model did you build?
4. What was your result?
5. What would you do next?

### Wrap-Up Slides

**Slide 15: What We Learned in 3 Days**
- Python basics
- Pandas for data manipulation
- EDA with statistics
- Data visualization
- Machine learning workflow

**Slide 16: You Are Not Done**
- This was a foundation
- University will deepen the math and theory
- Keep building projects

**Slide 17: 30-Day Post-Course Plan**

| Week | Focus |
|------|-------|
| Week 1 | Rebuild Day 1–3 notebooks from scratch |
| Week 2 | Complete 2 Kaggle "Getting Started" competitions |
| Week 3 | Learn Git; upload 3 projects to GitHub |
| Week 4 | Read one case study or watch one lecture per day |

**Slide 18: Resources**
- Kaggle Learn
- Google Colab
- scikit-learn documentation
- Pandas documentation
- StatQuest YouTube channel
- Codecademy / DataCamp Python courses

---

## Day 3 Live Coding Script

```python
# =====================================
# Day 3: Machine Learning Live Coding
# =====================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load data
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)

# Choose features
features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

# Preprocess
X["Age"] = X["Age"].fillna(X["Age"].median())
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})
print("\nFeature Importance:")
print(importance)
```

---

## GitHub Upload Instructions

1. Go to github.com and sign in
2. Click **New repository**
3. Name it `data-science-prep-projects`
4. Make it public
5. Click **Upload files**
6. Drag and drop the `.ipynb` notebook files
7. Add a README.md describing the projects

---

## Instructor Tips

- Keep ML theory light — focus on the workflow
- Emphasize that students should understand train/test split
- If someone finishes early, ask them to try a different model (Decision Tree)
- Encourage students to help each other
- End with confidence: they have now done real data science
