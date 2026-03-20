result = pd.concat([C, D]).drop_duplicates(subset='A', keep='last')
print(result)
