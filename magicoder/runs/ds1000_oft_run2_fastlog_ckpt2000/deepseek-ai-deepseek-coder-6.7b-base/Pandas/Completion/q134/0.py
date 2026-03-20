result = df.loc[df.duplicated(subset=['col1','col2'], keep='last')]
result['index_original'] = result.index

print(result)
