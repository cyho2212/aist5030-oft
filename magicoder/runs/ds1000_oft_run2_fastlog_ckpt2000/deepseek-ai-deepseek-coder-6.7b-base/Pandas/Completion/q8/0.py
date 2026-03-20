result = df.drop_duplicates(subset='url', keep='first')

print(result)
