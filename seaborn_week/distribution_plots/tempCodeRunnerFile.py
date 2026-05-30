import seaborn 
import matplotlib.pyplot as plt 
df = seaborn.load_dataset('tips')
custom_palette = {'Male': 'lightblue', 'Female': 'pink'}
seaborn.pairplot(df, hue='sex', palette=custom_palette)
plt.show()