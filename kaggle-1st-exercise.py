import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

all_data = pd.read_csv('googleplaystore.csv')


### Check for missing values & cleanse data
print(all_data.info())



### Columns analysis (missing values)
# Rating
ratings = all_data['Rating']
ratings.plot(kind='box', color='r')
plt.show()


print(all_data[all_data['Rating']>5])
all_data.drop([10472], inplace=True)

def input_median(series):
    return series.fillna(series.median())

all_data['Rating'] = all_data['Rating'].transform(input_median)
print(all_data['Type'].mode())
print(all_data['Current Ver'].mode())
print(all_data['Android Ver'].mode())

all_data['Type'].fillna(str(all_data['Type'].mode().values[0]), inplace=True)
all_data['Current Ver'].fillna(str(all_data['Current Ver'].mode().values[0]), inplace=True)
all_data['Android Ver'].fillna(str(all_data['Android Ver'].mode().values[0]), inplace=True)

print(all_data.info())



### Transform data type to numeric
all_data['Price'] = all_data['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
all_data['Price'] = all_data['Price'].apply(lambda x: float(x))
all_data['Reviews'] = pd.to_numeric(all_data['Reviews'], errors='coerce')
all_data['Installs'] = all_data['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else str(x))
all_data['Installs'] = all_data['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else str(x))
all_data['Installs'] = all_data['Installs'].apply(lambda x: float(x))

print(all_data.head())