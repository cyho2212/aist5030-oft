result = ''
for col in df.columns:
    result += f'---- {col} ----\n{df[col].value_counts()}\n\n'

print(result)
