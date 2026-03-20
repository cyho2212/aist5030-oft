result = df[df['A'].apply(lambda x: isinstance(x, str))]
print(result)
