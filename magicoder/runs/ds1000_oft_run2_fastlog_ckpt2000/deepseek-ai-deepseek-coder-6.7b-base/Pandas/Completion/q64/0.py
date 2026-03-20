result = df.groupby('name').ngroup()
result = result.rename('ID').reset_index()
result = result.drop('name', axis=1)
print(result)
