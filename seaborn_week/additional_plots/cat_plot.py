# example 1
import seaborn as sns 

exercise = sns.load_dataset("exercise")
g = sns.catplot(x="time", y="pulse",
                hue="kind", data=exercise)

# example 2
import seaborn as sns 
sns.set_theme(style="ticks")
exercise = sns.load_dataset("exercise")
g = sns.catplot(x="time", kind="count",
                data=exercise)