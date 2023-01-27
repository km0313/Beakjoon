from sklearn.datasets import load_iris
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
import seaborn as sns

iris = load_iris() 



df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())
print(df.isna().sum())
x_data=df.iloc[:,:-1]
y_data=df.iloc[:,[-1]]

sns.pairplot(df)
plt.show()