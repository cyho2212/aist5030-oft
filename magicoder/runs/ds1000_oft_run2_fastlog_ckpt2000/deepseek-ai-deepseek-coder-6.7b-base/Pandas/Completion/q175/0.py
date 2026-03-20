result = df[df['A'].apply(lambda x: isinstance(x, (int, float)))]

print(result)
