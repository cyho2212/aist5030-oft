result = pd.merge(C, D, how='outer', on='A')
result['duplicated'] = result['B_x'].notnull() & result['B_y'].notnull()
result = result.drop(['B_x', 'B_y'], axis=1)
result = result.rename(columns={'B_x': 'B'})

print(result)
