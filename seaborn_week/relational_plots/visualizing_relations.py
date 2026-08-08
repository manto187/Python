import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(style="darkgrid")

dataset = pd.read_csv('FuelConsumption.csv')

sns.relplot(x="ENGINESIZE", y="CO2EMISSIONS", data=dataset)