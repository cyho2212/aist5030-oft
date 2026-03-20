result = pd.concat([a, b, c], axis=1)
result = result.apply(tuple, axis=1)
result = pd.DataFrame(result.values.tolist(), columns=['one', 'two'])
print(result)
