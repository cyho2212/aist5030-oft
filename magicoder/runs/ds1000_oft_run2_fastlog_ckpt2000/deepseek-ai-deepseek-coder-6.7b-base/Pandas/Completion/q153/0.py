result = df.corr()
result = result.applymap(lambda x: 'one-to-one' if x == 1 else 'one-to-many' if x > 0 else 'many-to-one' if x < 0 else 'many-to-many')
print(result)
