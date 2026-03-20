
# Group by UserId and sample 20% of each group
df_sample = df.groupby('UserId').apply(lambda x: x.sample(frac=0.2, random_state=0))

# Set Quantity to 0 for the sampled rows
df_sample.loc[df_sample.index, 'Quantity'] = 0

# Reset index
df_sample = df_sample.reset_index(drop=True)

print(df_sample)
