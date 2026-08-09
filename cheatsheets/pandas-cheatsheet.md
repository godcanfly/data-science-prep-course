# Pandas Cheatsheet

## Import

```python
import pandas as pd
```

## Loading Data

```python
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
```

## Inspecting Data

```python
df.head()              # First 5 rows
df.head(10)            # First 10 rows
df.tail()              # Last 5 rows
df.shape               # (rows, columns)
df.columns             # Column names
df.info()              # Data types and missing values
df.describe()          # Summary statistics
df.dtypes                # Data types of each column
```

## Selecting Columns

```python
df["Name"]                              # Single column (Series)
df[["Name", "Age"]]                      # Multiple columns (DataFrame)
```

## Selecting Rows

```python
df.iloc[0]                              # First row by position
df.iloc[0:5]                            # First 5 rows by position
df.loc[0, "Name"]                       # Row by label, specific column
```

## Filtering

```python
df[df["Age"] > 30]
df[df["Sex"] == "female"]
df[(df["Age"] > 30) & (df["Sex"] == "female")]
df[(df["Age"] < 18) | (df["Fare"] > 100)]
```

## Sorting

```python
df.sort_values("Age")
df.sort_values("Age", ascending=False)
df.sort_values(["Pclass", "Age"])
```

## Adding / Modifying Columns

```python
df["NewColumn"] = df["A"] + df["B"]
df["AgeGroup"] = df["Age"].apply(lambda x: "Child" if x < 18 else "Adult")
```

## Dropping

```python
df = df.drop(columns=["Cabin"])
df = df.drop(index=0)
```

## Handling Missing Values

```python
df.isnull().sum()                       # Count missing per column
df.isnull().sum() / len(df) * 100     # Percentage missing

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Age"] = df["Age"].fillna(0)
df = df.dropna()                        # Drop rows with any missing value
df = df.dropna(subset=["Age"])        # Drop rows where Age is missing
```

## Aggregation

```python
df["Age"].mean()
df["Age"].median()
df["Age"].std()
df["Age"].min()
df["Age"].max()
df["Age"].count()

# Groupby
df.groupby("Sex")["Age"].mean()
df.groupby(["Sex", "Pclass"])["Survived"].mean()

df.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": ["mean", "max"],
    "Survived": "mean"
})
```

## Value Counts

```python
df["Sex"].value_counts()
df["Pclass"].value_counts(normalize=True)  # Percentages
```

## Unique Values

```python
df["Pclass"].unique()
df["Pclass"].nunique()
```

## Saving Data

```python
df.to_csv("cleaned_data.csv", index=False)
```

## Combining Conditions

| Operator | Meaning |
|---|---|
| `&` | AND |
| `\|` | OR |
| `~` | NOT |

Remember to wrap each condition in parentheses.

```python
df[(df["Age"] > 30) & (df["Sex"] == "female")]
```
