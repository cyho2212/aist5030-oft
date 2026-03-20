result = df.copy()
for col in df.columns:
    result[f'inv_{col}'] = 1 / df[col]

print(result)
