df['A'] = df['A'].fillna(method='ffill').fillna(method='bfill')
print(df)
