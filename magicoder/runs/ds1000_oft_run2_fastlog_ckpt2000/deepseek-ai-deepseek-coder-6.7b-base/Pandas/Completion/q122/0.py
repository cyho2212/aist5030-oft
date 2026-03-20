
# Calculate pairwise distances
df['distance'] = df.groupby('time')['x'].transform(lambda x: x.sub(df['x']).pow(2).add(df.groupby('time')['y'].transform(lambda y: y.sub(df['y']).pow(2))))

# Get the car with the minimum distance for each time
df['farmost_neighbour'] = df.groupby('time')['distance'].transform(lambda x: x.idxmin())

# Calculate the average distance for each time
df_avg = df.groupby('time')['distance'].mean()

# Print the results
print(df)
print(df_avg)
