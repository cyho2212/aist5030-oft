result = df[~((99 <= df['closing_price']) & (df['closing_price'] <= 101))]

print(result)
