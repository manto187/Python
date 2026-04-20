# plotting with only matplotlib
import matplotlib.pyplot as plt 

plt.plot([0,1], [10, 11], label = 'line 1')
plt.plot([0, 1], [11, 10], label = 'line 2')
plt.scatter([0, 1], [10.5, 10.5], color = 'blue', marker='o', label='Dots')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('simple line and dot plot')
plt.legend()
plt.show()

# enhancing matplotlib with seaborn styles

import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_theme(style = "darkgrid")

x = [1,2,3,4,5]
y = [10,12,15,18,22]

plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Trend")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("matplotlib plot with seaborn theme")
plt.legend()
plt.show()

# customizing plots with matplotlib 

import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

data = pd.DataFrame({
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [100, 150, 200, 250, 300]
})

plt.figure(figsize=(8, 5))
sns.lineplot(x='year', y='sales', data=data, marker='o')

plt.title("yearly sales growth", fontsize = 14, fontweight = 'bold')
plt.xlabel("year", fontsize=12)
plt.ylabel("total sales", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='-')
plt.show()


# overlaying seaborn and matplotlib plots

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

x = np.linspace(0, 10, 20)
y = np.sin(x)

plt.figure(figsize=(8,5))

sns.lineplot(x=x, y=y, color='blue', label='sine wave')

plt.scatter(x, y, color='red', marker='o', label="data points")

plt.title("seaborn line plot with matplotlib scatter overlay")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

# enhancing seaborn histogram with matplotlib annotations"abs

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = np.random.randn(1000)
plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True, bins=30, color='purple')

mean_value=np.mean(data)
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2)
plt.text(mean_value+0.1, 50, f'Mean: {mean_value:.2f}', color='red')

plt.title("distribution with seaborn and matplotlib customization")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()