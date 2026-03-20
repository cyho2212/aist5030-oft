result = df.sort_values('keep_if_dup', ascending=False).drop_duplicates('url', keep='first')

print(result)
