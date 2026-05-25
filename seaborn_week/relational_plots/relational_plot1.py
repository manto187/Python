import seaborn as sns
data = sns.load_dataset('tips')

print(data.head())


# visualizing most basic plot to show all the data points in tips dataset
import seaborn as sns 
sns.set(style="ticks")
tips = sns.load_dataset('tips')
sns.replot(x="total_bill", y="tip", data=tips)


# grouping data points on basis of category, here as time 
import seaborn as sns
sns.set(style="ticks")
tips = sns.load_dataset('tips')
sns.replot(x="total_bill",
            y="tip",
            hue="time",
              data=tips)




#using time and sex for determinig the facet of the grid 
import seaborn as sns

sns.set(style ="ticks")

tips = sns.load_dataset('tips')

sns.relplot(x="total_bill", 
            y="tip",
            hue="day",
            col="time",
            row="sex",
            data=tips)
