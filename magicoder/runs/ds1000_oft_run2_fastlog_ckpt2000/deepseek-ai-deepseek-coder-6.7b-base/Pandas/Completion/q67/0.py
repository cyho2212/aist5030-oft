df = df.melt(id_vars=['user', 'someBool'], var_name='date', value_name='value')
df = df.dropna()

print(df)
