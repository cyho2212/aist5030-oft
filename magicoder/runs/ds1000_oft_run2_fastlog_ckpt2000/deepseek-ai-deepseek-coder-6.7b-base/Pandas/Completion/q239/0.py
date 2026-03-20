result = pd.concat([df1, df2], axis=0)
result = result.sort_values(by=['id', 'date'])
result = result.reset_index(drop=True)
print(result)
