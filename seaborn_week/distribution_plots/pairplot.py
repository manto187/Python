# example 1 
import seaborn 
import matplotlib.pyplot as plt 
df = seaborn.load_dataset('tips')
seaborn.pairplot(df, hue='day')
plt.show()


# example 2 
import seaborn 
import matplotlib.pyplot as plt 
df = seaborn.load_dataset('tips')
custom_palette = {'Male': 'lightblue', 'Female': 'pink'}
seaborn.pairplot(df, hue='sex', palette=custom_palette)
plt.show()

# example 3 
import seaborn 
import matplotlib.pyplot as plt 
df = seaborn.load_dataset('tips')
seaborn.pairplot(df[['total_bill', 'tips', 'size']])
plt.show()