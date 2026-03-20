result = df.loc[df['value'] < thresh]
result.loc['X'] = result['value'].mean()
result = result.reset_index()
print(result)
