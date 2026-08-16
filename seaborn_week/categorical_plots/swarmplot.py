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