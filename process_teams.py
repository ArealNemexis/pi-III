import pandas as pd

df = pd.read_csv('result.csv')

# print(df['name'].value_counts())
# print(df.query("teamWin == 'TRUE'"))

# print(df.loc[df['teamWin'] == True]['name'].value_counts()) # ganharam mais series
# print(df.loc[df['teamWin'] == False]['name'].value_counts()) # perderam mais series
# print(df.loc[df['rounsWin'] > 2][['name', 'rounsWin']].groupby('name').sum()) # numero de rounds ganhos
