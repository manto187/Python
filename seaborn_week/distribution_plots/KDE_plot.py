import pandas as pd 
import seaborn as sns
import numpy as np 
from matplotlib import pyplot as plt

x=np.random.randn(200)
y=np.random.randn(200)
sns.kdeplot(x)
sns.kdeplot(y)
sns.kdeplot(x, shade=True)
sns.kdeplot(x,shade=True,color="Green")
sns.kdeplot(x, vertical=True)
sns.kdeplot(x,y)
sns.kdeplot(x,y,shade=True)
sns.kdeplot(x,y,cmap="winter_r")
sns.kdeplot(x,y, shade=True, cbar=True)

# for iris dataset
iris = sns.load_dataset("iris")
iris
setosa=iris.loc[iris.species=="setosa"]
viriginica=iris.loc[iris.species=="viriginica"]
sns.kdeplot(setosa.petal_length, setosa.petal_width)

sns.kdeplot(setosa.sepal_width, setosa.sepal_length)

# two separate kdeplots with different variables 
sns.kdeplot(setosa.petal_length, setosa.petal_width)
sns.kdeplot(viriginica.petal_length, viriginica.petal_width)