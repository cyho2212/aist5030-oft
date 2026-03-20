
# Get value counts for each column
value_counts = df.apply(pd.Series.value_counts)

# Create a mask for values that appear at least twice
mask = value_counts >= 2

# Replace values that appear less than twice with 'other'
df = df.where(mask, 'other')

# Print the result
print(df)
