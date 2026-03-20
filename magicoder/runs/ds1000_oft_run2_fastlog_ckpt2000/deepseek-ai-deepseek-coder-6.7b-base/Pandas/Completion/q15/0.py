result = pd.concat([df, df['message'].str.extractall('(?P<key>\w+):\s*(?P<value>\w+)')], axis=1)
result = result.drop('message', axis=1)
result = result.pivot(index=['name', 'status', 'number'], columns='key', values='value').reset_index()
result = result.fillna('none')

print(result)
