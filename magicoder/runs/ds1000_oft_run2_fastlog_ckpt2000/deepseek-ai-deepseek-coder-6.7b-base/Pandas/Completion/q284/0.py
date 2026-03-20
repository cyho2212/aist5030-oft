
# Create a new column 'frequent'
df['frequent'] = df.mode(axis=1)[0]

# Create a new column 'freq_count'
df['freq_count'] = df.mode(axis=1)[0].value_counts()

print(df)
