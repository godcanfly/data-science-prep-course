# Datasets for the Course

All datasets are freely available online. Use the links below or download from Kaggle.

---

## 1. Titanic Dataset

**Best for**: Classification, survival prediction

**Sources**:
- Primary CSV: `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv`
- Course snapshot: `datasets/titanic.csv`
- Snapshot SHA-256: `81787d320d7f7b03df935e91de8bd19e11d45c5bbcab86ef4d4a76dc91b7d4f2`
- Upstream project: `https://github.com/mwaskom/seaborn-data`

**Columns**: survived, pclass, sex, age, sibsp, parch, fare, embarked, class, who, adult_male, deck, embark_town, alive, alone

The notebooks try the primary URL first and fall back to the local snapshot when the network is unavailable. They validate the exact 891-row, 15-column schema before analysis.

---

## 2. Iris Dataset

**Best for**: Multi-class classification

**Sources**:
- scikit-learn built-in
- Seaborn: `sns.load_dataset("iris")`
- UCI Machine Learning Repository

**Columns**: sepal_length, sepal_width, petal_length, petal_width, species

---

## 3. California Housing Dataset

**Best for**: Regression

**Sources**:
- scikit-learn built-in: `fetch_california_housing()`

**Columns**: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, target (MedHouseVal)

---

## 4. Other Datasets for Practice

| Dataset | Source | Good For |
|---|---|---|
| Palmer Penguins | `seaborn.load_dataset("penguins")` | Classification, EDA |
| Tips | `seaborn.load_dataset("tips")` | Regression, EDA |
| Diamonds | `seaborn.load_dataset("diamonds")` | Regression, visualization |
| MPG | `seaborn.load_dataset("mpg")` | Regression, EDA |

---

## How to Load Datasets in Colab

### From URL
```python
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
```

### From Seaborn
```python
import seaborn as sns
df = sns.load_dataset("titanic")
```

### From scikit-learn
```python
from sklearn.datasets import load_iris
iris = load_iris(as_frame=True)
df = iris.frame
```

### Upload local file
1. In Colab, click the folder icon on the left
2. Click the upload button
3. Use: `pd.read_csv("filename.csv")`
