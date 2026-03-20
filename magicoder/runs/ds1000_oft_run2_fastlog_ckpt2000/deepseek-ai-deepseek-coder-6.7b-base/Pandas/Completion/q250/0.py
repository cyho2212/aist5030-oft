result = df.filter(like=s, axis=1)

# Rename columns
result.columns = [f'{s}{i}' for i in range(1, len(result.columns)+1)]

print(result)
