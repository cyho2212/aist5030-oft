
# Calculate the number of NaN values
num_nan = df['Column_x'].isna().sum()

# Calculate the number of values to fill with 0
num_0 = int(num_nan * 0.3)

# Calculate the number of values to fill with 0.5
num_05 = int(num_nan * 0.3)

# Calculate the number of values to fill with 1
num_1 = num_nan - num_0 - num_05

# Fill the NaN values
df['Column_x'] = df['Column_x'].fillna(0, limit=num_0)
df['Column_x'] = df['Column_x'].fillna(0.5, limit=num_05)
df['Column_x'] = df['Column_x'].fillna(1, limit=num_1)

print(df)
