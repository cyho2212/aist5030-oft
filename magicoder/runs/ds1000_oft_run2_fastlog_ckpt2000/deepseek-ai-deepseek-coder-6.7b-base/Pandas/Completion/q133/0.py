
# Find duplicates
duplicate_bool = df.duplicated(subset=['col1','col2', '3col'], keep='first')

# Add index_original column
df['index_original'] = df.index

# Filter duplicates
duplicate = df.loc[duplicate_bool == True]

print(duplicate)
