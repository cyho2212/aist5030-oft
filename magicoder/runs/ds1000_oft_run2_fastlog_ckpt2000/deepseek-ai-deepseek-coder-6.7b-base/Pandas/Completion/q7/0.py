result = df.drop_duplicates(subset='url', keep='first')

# Print the result
print(result)
