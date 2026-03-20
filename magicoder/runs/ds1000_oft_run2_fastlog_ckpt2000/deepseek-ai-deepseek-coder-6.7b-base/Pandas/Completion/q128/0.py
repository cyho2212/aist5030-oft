
# Select 20% of rows
df_sample = df.sample(frac=0.2, random_state=0)

# Set ProductId to 0
df_sample['ProductId'] = 0

# Merge the original DataFrame with the sampled DataFrame
df_result = pd.concat([df, df_sample]).drop_duplicates(keep=False)

print(df_result)
