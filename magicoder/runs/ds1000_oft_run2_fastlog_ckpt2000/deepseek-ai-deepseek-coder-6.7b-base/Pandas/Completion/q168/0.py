
# Softmax normalization
df['softmax'] = df.groupby('a')['b'].transform(lambda x: x / x.sum())

# Min-max normalization
df['min-max'] = df.groupby('a')['b'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

print(df)
