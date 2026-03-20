result = df.groupby('b').agg({'a': ['mean', 'std']})
print(result)
