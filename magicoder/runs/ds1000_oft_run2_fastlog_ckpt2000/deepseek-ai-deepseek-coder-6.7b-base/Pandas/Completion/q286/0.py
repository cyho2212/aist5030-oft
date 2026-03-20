
# Create a new column 'frequent'
df['frequent'] = df.apply(lambda x: x.value_counts().index.tolist(), axis=1)

# Create a new column 'freq_count'
df['freq_count'] = df.apply(lambda x: x.value_counts().max(), axis=1)

print(df)
