# Datasets for the Course

All datasets are freely available online. Use the links below or download from Kaggle.

---

## 1. Titanic Dataset

**Best for**: Classification, survival prediction

**Sources**:
- Direct CSV: `https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv`
- Kaggle: `https://www.kaggle.com/c/titanic`
- Seaborn built-in: `sns.load_dataset("titanic")`

**Columns**: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

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
url = "https://raw.githubusercontent.com/datasciencedoc/data/master/titanic.csv"
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
