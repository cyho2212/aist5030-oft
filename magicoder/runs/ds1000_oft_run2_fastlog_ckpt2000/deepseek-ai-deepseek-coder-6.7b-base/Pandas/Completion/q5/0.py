
# Create a dictionary to map old values to new values
mapping = {'apple': 'other', 'potato': 'other', 'cheese': 'cheese', 'banana': 'other', 'egg': 'other'}

# Apply the mapping to the dataframe
df = df.replace(mapping)

# Print the result
print(df)
