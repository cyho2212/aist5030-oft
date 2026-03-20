
# Create a new column 'frequent'
df['frequent'] = df.mode(axis=1)[0]

# Create a new column 'freq_count'
df['freq_count'] = df.apply(lambda row: row.value_counts().max(), axis=1)

print(df)
