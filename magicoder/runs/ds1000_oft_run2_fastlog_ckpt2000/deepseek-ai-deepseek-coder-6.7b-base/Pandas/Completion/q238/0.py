result = pd.concat([df1, df2], axis=0)
result['date'] = pd.to_datetime(result['date'], format='%Y/%m/%d').dt.strftime('%d-%b-%Y')
result = result.sort_values(['id', 'date'])
print(result)
