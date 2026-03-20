result = df.corr().applymap(lambda x: 'one-2-one' if x == 1 else 'many-2-many' if x == -1 else 'one-2-many' if x == 0 else 'many-2-one')

print(result)
