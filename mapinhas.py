import pandas as pd

df = pd.read_csv('result.csv')

print(df['Overpass'].value_counts())