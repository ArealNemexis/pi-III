import pandas as pd

df = pd.read_csv('csvs/merged.csv')

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = value + dict_1[key]
   return dict_3


# unique_teams = set(pd.unique(df['team1']))
# unique_teams.add(pd.unique(df['team2']))

# print(len(unique_teams))

# print(len(set(pd.unique(df['team1']).tolist() + pd.unique(df['team2']).tolist())))
# print(len(pd.unique(df['team2'])))

# occurrences = df['team1'] + df['team2']
vc1 = df['team1'].value_counts()
vc2 = df['team2'].value_counts()
# occurrences = df['team1'].value_counts() + df['team2'].value_counts()


# print(vc1.to_dict())
# print(vc2)

matches_per_team = mergeDictionary(vc1.to_dict(), vc2.to_dict())


# partidas jogadas por cada time, vai virar um grafico
df2 = pd.DataFrame(pd.Series(matches_per_team))
df2.to_csv("teste.csv")