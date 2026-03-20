result = df.groupby('key1')['key2'].apply(lambda x: (x == 'one').sum()).reset_index(name='count')

print(result)
