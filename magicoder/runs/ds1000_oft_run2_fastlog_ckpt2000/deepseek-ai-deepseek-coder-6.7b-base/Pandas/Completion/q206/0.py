df['label'] = df['Close'].diff().gt(0).astype(int)
df.loc[0, 'label'] = 1

print(df)
