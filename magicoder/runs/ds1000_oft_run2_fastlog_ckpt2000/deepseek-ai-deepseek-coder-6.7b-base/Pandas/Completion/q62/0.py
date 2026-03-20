result = df.groupby('name').ngroup() + 1
df['a'] = result
print(df)
