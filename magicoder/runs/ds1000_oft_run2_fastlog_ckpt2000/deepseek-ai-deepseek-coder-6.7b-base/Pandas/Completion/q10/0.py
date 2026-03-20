result = {}
for name, group in df.groupby('name'):
    result[name] = group.set_index('v1').T.to_dict('index')

print(result)
