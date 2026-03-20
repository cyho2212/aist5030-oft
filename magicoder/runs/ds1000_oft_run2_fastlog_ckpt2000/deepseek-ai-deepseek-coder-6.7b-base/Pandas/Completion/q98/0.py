df_filtered = df.loc[df.abs().max(axis=1) > 1]
print(df_filtered)
