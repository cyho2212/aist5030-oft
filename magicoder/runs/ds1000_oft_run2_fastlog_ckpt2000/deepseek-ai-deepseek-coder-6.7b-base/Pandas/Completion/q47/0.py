result = df.loc[df['value'] < thresh]
result['value'] = result['value'].sum()
result = result.reset_index()
result.loc[0, 'lab'] = 'X'
result = result.set_index('lab')
print(result)
