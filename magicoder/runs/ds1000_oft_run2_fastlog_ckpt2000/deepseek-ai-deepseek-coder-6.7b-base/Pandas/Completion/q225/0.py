
# Calculate the number of NaN values
num_nan = df['Column_x'].isna().sum()

# Calculate the number of 0s and 1s
num_zeros = (df['Column_x'] == 0).sum()
num_ones = (df['Column_x'] == 1).sum()

# Calculate the number of 0s and 1s to fill
num_zeros_to_fill = num_nan // 2
num_ones_to_fill = num_nan // 2

# Fill the NaN values with 0s
df['Column_x'].fillna(0, inplace=True)

# Fill the remaining NaN values with 1s
df['Column_x'].fillna(1, inplace=True)

# Fill the first num_zeros_to_fill NaN values with 0s
df['Column_x'].iloc[:num_zeros_to_fill] = 0

# Fill the remaining num_ones_to_fill NaN values with 1s
df['Column_x'].iloc[num_zeros:] = 1

print(df)
