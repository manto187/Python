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