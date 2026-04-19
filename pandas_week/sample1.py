import pandas
mydataset = {
    'cars': ["bmw", "volvo", "ford"],
    'passings':[3,7,2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
# aliasing pandas as pd
import pandas as pd
data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)


# checking pandas version

print(pd.__version__)