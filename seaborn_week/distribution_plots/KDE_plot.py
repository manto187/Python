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
