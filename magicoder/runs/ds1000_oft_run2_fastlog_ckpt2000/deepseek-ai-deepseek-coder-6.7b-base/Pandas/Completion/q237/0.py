result = pd.concat([df1, df2], axis=0)
result['city'] = result['city'].fillna(method='ffill')
result['district'] = result['district'].fillna(method='ffill')
print(result)
