result = df.loc[df['c'] > 0.45, columns]

# Convert to numpy array
training_set = result.values
