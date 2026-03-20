
# Create a dictionary to map values to their counts
counts = {}
for col in df.columns:
    counts[col] = df[col].value_counts()

# Create a dictionary to map values to their replacement
replacements = {}
for col in df.columns:
    replacements[col] = counts[col][counts[col] >= 2].index.tolist()

# Replace values
for col in df.columns:
    df[col] = df[col].replace(replacements[col], 'other')

# Replace 'apple' with 'other'
df['Qu1'] = df['Qu1'].replace('apple', 'other')

# Print the result
print(df)
