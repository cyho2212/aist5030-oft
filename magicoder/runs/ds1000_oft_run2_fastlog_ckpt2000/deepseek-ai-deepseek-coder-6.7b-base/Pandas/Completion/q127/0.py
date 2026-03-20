
# Select 20% of rows
sample_df = df.sample(frac=0.2, random_state=0)

# Set Quantity to 0
sample_df['Quantity'] = 0

# Merge the original DataFrame with the sample DataFrame
result_df = df.merge(sample_df, how='left', on=['UserId', 'ProductId'])

# Fill NaN values with original Quantity
result_df['Quantity'] = result_df['Quantity_x'].fillna(result_df['Quantity_y'])

# Drop the temporary columns
result_df.drop(['Quantity_x', 'Quantity_y'], axis=1, inplace=True)

print(result_df)
