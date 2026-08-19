import seaborn 

seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")

seaborn.swarmplot(x="timepoint",
                  y="signal",
                  data=fmri)


# example 2 
import seaborn
seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")

seaborn.swarmplot(x="timepoint",
                  y="signal",
                  hue="region",
                  data=fmri)



# example 3 
import seaborn

seaborn.set(style="whitegrid")
tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x=tips["total_bill"])

# example 4 
import seaborn

seaborn.set(style="whitegrid")
tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="total_bill", y="day", data=tips)


import seaborn 

seaborn.set(style="whitegrid")

tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="day", y="total_bill", hue="time", data=tips)

# example 5 

import seaborn 

seaborn.set(style="whitegrid")

tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="day", y="total_bill", data=tips, linewidth=2)

# example 6
import seaborn 
seaborn.set(style="whitegrid")

tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="day", y="total_bill", hue="smoker",
                  data=tips, palette="Set2", size=20, marker="D",
                  edgecolor="gray", alpha=.25)

# example 7
import seaborn 
seaborn.set(style="whitegrid")

tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="time", y="tip",
                  data=tips, order=["Dinner", "Lunch"])


# example 8
import seaborn 
seaborn.set(style="whitegrid")

tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="time", y="tips", data=tips,
                  hue='smoker', size=10)


 # example 9
import seaborn 
seaborn.set(style="whitegrid")

tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x='day', y='total_bill', data=tips,
                  hue='time', palette='pastel')