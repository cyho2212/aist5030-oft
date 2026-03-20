
# Get value counts for each column
value_counts = df.apply(pd.Series.value_counts)

# Create a mask for values that have at least 3 appearances
mask = value_counts >= 3

# Replace values in df with 'other' where mask is False
df.loc[~mask] = 'other'

# Print the result
print(df)
