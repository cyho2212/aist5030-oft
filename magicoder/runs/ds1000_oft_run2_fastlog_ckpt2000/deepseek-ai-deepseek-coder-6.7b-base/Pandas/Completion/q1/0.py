result = df.iloc[List]

# Counting the number of rows with different Type
original_types = df['Type'].unique()
result_types = result['Type'].unique()
different_types = len(set(original_types) ^ set(result_types))

print(result)
print(different_types)
