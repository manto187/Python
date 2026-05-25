import seaborn as sns

from matplotlib_week import markers 
sns.set(style="ticks")

tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tips", data=tips)

# using relplot() with kind="scatter" to create a scatter plot of total bill vs tip amount in the tips dataset
import seaborn as sns
sns.set(style ="ticks") 
tips = sns.load_dataset('tips')

sns.relplot(x ="total_bill",
            y ="tip",
            kind ="scatter", 
            data = tips)

# using relplot() with kind="line" to create a line plot of total bill vs tip amount in the tips dataset
import seaborn as sns   
sns.set(style="ticks")
tips = sns.load_dataset('tips')

sns.relplot(x="total_bill",
            y="tips",
            kind="line",
            data=tips)


# plotting a scatterplot using  marker to differentiate between timing of the people visiting the restaurant
import seaborn as sns 

sns.set(style="ticks")
tips = sns.load_dataset('tips')
markers = {"Lunch": "o", "Dinner": "s"}
sns.relplot(x="total_bill",
            y="tip",
            hue="time",
            markers=markers,
            data=tips)


