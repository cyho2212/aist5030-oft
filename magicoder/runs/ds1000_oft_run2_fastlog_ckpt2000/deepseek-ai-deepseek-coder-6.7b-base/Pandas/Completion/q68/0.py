result = df.loc[df['c'] > 0.5, columns]

# Convert to numpy array
training_set = result.values
