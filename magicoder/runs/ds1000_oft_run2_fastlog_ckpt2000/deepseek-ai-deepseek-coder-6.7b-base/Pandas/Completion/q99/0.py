df_filtered = df.loc[df.filter(like='Value_').abs().any(axis=1)]
df_filtered = df_filtered.rename(columns=lambda x: x.split('_')[1])
print(df_filtered)
