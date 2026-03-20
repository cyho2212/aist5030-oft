
# Calculate the number of NaN values
num_nan = df['Column_x'].isna().sum()

# Calculate the number of values to fill with 0
num_to_fill_0 = int(num_nan * 0.5)

# Calculate the number of values to fill with 1
num_to_fill_1 = num_nan - num_to_fill_0

# Fill the NaN values with 0
df['Column_x'].fillna(0, inplace=True, limit=num_to_fill_0)

# Fill the remaining NaN values with 1
df['Column_x'].fillna(1, inplace=True, limit=num_to_fill_1)

print(df)
