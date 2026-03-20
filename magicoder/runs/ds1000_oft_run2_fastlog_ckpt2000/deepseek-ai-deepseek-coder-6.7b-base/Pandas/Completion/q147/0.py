df['cumsum'] = df.groupby('id')['val'].cumsum()
df.loc[df['cumsum'] < 0, 'cumsum'] = 0

print(df)
