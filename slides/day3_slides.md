# Day 3 Slides Outline

## Slide 1: What is Machine Learning?
- Traditional programming: human writes rules
- ML: computer learns patterns from data
- Input + answers → model → predictions

## Slide 2: The ML Recipe
1. Collect data
2. Prepare/clean data
3. Choose a model
4. Train on training data
5. Test on new data
6. Evaluate and improve

## Slide 3: Supervised Learning
- Labeled examples
- Classification: predict category
- Regression: predict number

## Slide 4: Unsupervised Learning
- No labels
- Find patterns or groups

## Slide 5: Features and Target
- X = features = inputs
- y = target = what we predict

## Slide 6: Train/Test Split
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## Slide 7: Overfitting vs Underfitting
- Underfitting: too simple
- Overfitting: memorizes training data
- Goal: balance

## Slide 8: Prepare Data for ML
- Select features
- Handle missing values
- Convert text to numbers

## Slide 9: Train a Model
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

## Slide 10: Make Predictions
```python
predictions = model.predict(X_test)
```

## Slide 11: Accuracy
```python
accuracy_score(y_test, predictions)
```

## Slide 12: Confusion Matrix
- True/False Positives/Negatives

## Slide 13: Precision and Recall
- Precision: predicted survivors who really survived
- Recall: actual survivors we found

## Slide 14: Feature Importance
- Which features matter most?

## Slide 15: Capstone Project Options
- Titanic survival prediction
- Iris flower classification
- House price prediction

## Slide 16: Capstone Requirements
- Load and explore data
- Clean and prepare features
- Create 3+ visualizations
- Build and evaluate model
- Write conclusions
- Upload to GitHub

## Slide 17: Capstone Work Plan
- 15:00–15:20: Load and explore
- 15:20–15:50: Clean and prepare
- 15:50–16:10: Train model
- 16:10–16:25: Evaluate and visualize
- 16:25–16:30: Finalize

## Slide 18: Presentation Format
1. Problem
2. Data
3. Analysis
4. Model
5. Results
6. Next steps

## Slide 19: What We Learned in 3 Days
- Python, Pandas, EDA, visualization, ML workflow

## Slide 20: You Are Not Done
- This was a foundation
- University will deepen the math and theory

## Slide 21: 30-Day Post-Course Plan
- Week 1: Rebuild notebooks
- Week 2: Kaggle competitions
- Week 3: GitHub portfolio
- Week 4: Read case studies

## Slide 22: Resources
- Kaggle Learn
- Google Colab
- scikit-learn docs
- Pandas docs
- StatQuest YouTube

## Slide 23: Final Message
- Data science is about asking good questions
- Keep building projects
- You have already started
