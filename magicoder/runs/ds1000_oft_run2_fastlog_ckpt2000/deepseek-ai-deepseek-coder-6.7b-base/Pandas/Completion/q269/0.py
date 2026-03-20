df = df.stack().reset_index(level=0).rename(columns={'level_0':'index',0:'value'})
df = df.pivot(index='index', columns='level_1', values='value')
df.columns = [f'{col}_{i+1}' for i, col in enumerate(df.columns)]
df = df.reset_index(drop=True)
print(df)
