df = pd.melt(df, id_vars=['Country', 'Variable'], var_name='year', value_name='value')
df = df.sort_values('year', ascending=False)
df = df.reset_index(drop=True)
print(df)
