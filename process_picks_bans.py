import pandas as pd

df = pd.read_csv('result.csv')

maps = ['Vertigo', 'Overpass', 'Mirage',
        'Inferno', 'Ancient', 'Dust2', 'Nuke']

picks_bans_df = pd.DataFrame(columns=['map_name','removed','picked','left'])

for map in maps:
    counted_uniques = df[map].value_counts()
    picks_bans_df.loc[len(picks_bans_df.index)+1] = [map, counted_uniques['removed'], counted_uniques['picked'], counted_uniques['left']]

print(picks_bans_df)
picks_bans_df.to_csv("picks_banks.csv")