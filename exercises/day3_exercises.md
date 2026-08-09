# Day 3 Exercises: Machine Learning + Capstone

## Exercise 1: ML Concepts (10 minutes)

Answer these questions in your own words:
1. What is the difference between supervised and unsupervised learning?
2. What is the difference between classification and regression?
3. Why do we split data into training and testing sets?
4. What is overfitting?

---

## Exercise 2: Train/Test Split (10 minutes)

Given a DataFrame `df` with features `X` and target `y`, write the code to split the data into 80% training and 20% testing, with `random_state=42`.

---

## Exercise 3: Build Your First Model (20 minutes)

Using the Titanic dataset, build a model to predict survival.

Use these features: `Pclass`, `Sex`, `Age`, `Fare`

Steps:
1. Load the data
2. Prepare features and target
3. Handle missing values
4. Convert `Sex` to numbers
5. Split into train/test
6. Train a `LogisticRegression` model
7. Predict on the test set
8. Print the accuracy

---

## Exercise 4: Evaluate the Model (10 minutes)

For the model you built in Exercise 3:
1. Print the confusion matrix
2. Print the classification report
3. Identify which class the model predicts better: survivors or non-survivors

---

## Exercise 5: Feature Importance (10 minutes)

Create a DataFrame showing each feature and its coefficient from the logistic regression model.

Which feature has the largest positive impact on survival prediction?

---

## Exercise 6: Try a Different Model (15 minutes)

Train a `DecisionTreeClassifier` on the same data. Compare its accuracy to the logistic regression model.

```python
from sklearn.tree import DecisionTreeClassifier
```

---

## Exercise 7: Capstone Project (60–90 minutes)

Choose one of the projects in the `projects/` folder and complete it end-to-end.

Your final notebook should include:
1. Introduction and question
2. Data loading and overview
3. Data cleaning
4. Exploratory analysis with at least 3 charts
5. Model building and evaluation
6. Conclusions and next steps

---

## Exercise 8: Upload to GitHub (15 minutes)

1. Create a new repository on GitHub
2. Upload your capstone notebook
3. Add a README.md describing the project
4. Share the link

---

## Bonus Challenge

Add `Embarked` as a feature. You will need to convert it to numbers first.

Hint: use `pd.get_dummies()` or `.map()`.
