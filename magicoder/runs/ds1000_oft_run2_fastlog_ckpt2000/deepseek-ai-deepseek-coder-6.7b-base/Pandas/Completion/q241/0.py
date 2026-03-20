result = pd.concat([C, D]).drop_duplicates(subset='A', keep='first')
print(result)
