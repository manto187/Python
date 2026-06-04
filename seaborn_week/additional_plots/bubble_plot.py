import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

data = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

df = pd.read_csv(data)
df.head()

# depict scatterplot illustration
sns.set_context("talk", font_scale=1.1)
plt.figure(figsize=(8,6))
sns.scatterplot(x="sepal.length",
                y="sepal.width",
                data=df)

plt.xlabel("Sepal.Length")
plt.ylabel("sepal.width")

# bubble plot with seaborn scatterplot()
sns.set_contex("talk", font_scale=1.1)
plt.figure(figsize=(10,6))
sns.scatterplot(x="petal.length",
                y="petal.width",
                data=df)

plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
plt.xlabel("petal.length")
plt.ylabel("petal.width")
plt.tight_layout()
plt.savefig("Bubble_plot_Seaborn_scatterplot.png",
            format='png', dpi=150)



# bubble plot with explicit size ranges seaborn scatterplot()
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

data = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

df = pd.read_csv(data)

df.head()

sns.set_context("talk", font_scale=1.2)
plt.figure(figsize=(10,6))
sns.scatterplot(x='sepal.length',
                y='sepal.width',
                sizes=(20,500),
                alpha=0.5,
                hue='variety',
                data=df)

plt.legend(bbox_to_anchor=(1.01,1),
borderaxespad=0)

plt.xlabel("sepal.length")
plt.ylabel("sepal.width")
plt.title("bubble plot with colors in seaborn")

plt.tight_layout()

                