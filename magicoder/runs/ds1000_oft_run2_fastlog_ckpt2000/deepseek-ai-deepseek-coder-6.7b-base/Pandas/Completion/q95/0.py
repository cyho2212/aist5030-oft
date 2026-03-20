df = pd.melt(df, id_vars=['Country', 'Variable'], var_name='year', value_name='value')
df = df.pivot(index=['Country', 'Variable', 'year'], columns='Variable', values='value').reset_index()
df.columns.name = None

print(df)
