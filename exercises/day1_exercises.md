# Day 1 Exercises: Python + Pandas

## Exercise 1: Variables (5 minutes)

Create variables for:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you like data science (boolean)

Print all four variables.

---

## Exercise 2: List Operations (10 minutes)

Given this list of test scores:

```python
scores = [72, 88, 91, 67, 95, 83]
```

Write code to:
1. Print the first score
2. Print the last score
3. Add a new score of 78
4. Print the total number of scores
5. Print the highest and lowest scores

---

## Exercise 3: Loops (10 minutes)

Use a `for` loop to print each score from the `scores` list with a 5% bonus added.

Example output:
```
75.6
92.4
95.55
...
```

---

## Exercise 4: Functions (10 minutes)

Write a function called `calculate_average` that takes a list of numbers and returns the average.

Test it with the `scores` list.

---

## Exercise 5: Dictionaries (10 minutes)

Create a dictionary for a movie with these keys: `title`, `year`, `director`, `rating`.

Then:
1. Print the title
2. Add a key `genre`
3. Print the entire dictionary

---

## Exercise 6: Pandas Basics (15 minutes)

Run the following code to load the Titanic dataset:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
df = pd.read_csv(url)
```

Then answer these questions with code:
1. How many rows and columns are there?
2. What are the column names?
3. Show the first 8 rows.
4. Show summary statistics for numeric columns.

---

## Exercise 7: Filtering (15 minutes)

Using the Titanic dataset:
1. Select only passengers who are female.
2. Select only passengers who paid more than 50 for their fare.
3. Select only passengers who are in first class (`Pclass == 1`) and survived.
4. Sort the data by age from oldest to youngest.

---

## Exercise 8: Groupby (15 minutes)

Using the Titanic dataset:
1. What is the average age of passengers?
2. What is the survival rate by passenger class?
3. What is the average fare by embarkation port (`Embarked`)?

---

## Bonus Challenge

Create a new column called `AgeGroup` where:
- `"Child"` if age < 18
- `"Adult"` if age is 18–60
- `"Senior"` if age > 60

Hint: use `df["Age"].apply()` with a function.
