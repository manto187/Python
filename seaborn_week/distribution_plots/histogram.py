import numpy as np 
import seaborn as sns 
import pandas as pd 

np.random.seed(1)
num_var = np.random.randn(1000)
num_var = pd.Series(num_var,name="numerical variable")
sns.histplot(data = num_var, kde = True)

# 2. dataset showing characteristics of different penguin species
import numpy as np 
import pandas as pd 
import seaborn as sns 

penguins = sns.load_dataset("penguins")

sns.histplot(data = penguins, x = "body_mass_g", kde=True)