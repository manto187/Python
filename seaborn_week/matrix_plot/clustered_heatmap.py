# Importing the library
import seaborn as sns
from sunbird.categorical_encoding import frequency_encoding

data = sns.load_dataset('flights')

frequency_encoding(data, 'month')

sns.clustermap(data, figsize=(7, 7))