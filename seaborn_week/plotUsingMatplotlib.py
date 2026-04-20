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