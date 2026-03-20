result = df.groupby('user').agg(lambda x: list(zip(x['time'], x['amount'])))

# Print the result
print(result)
