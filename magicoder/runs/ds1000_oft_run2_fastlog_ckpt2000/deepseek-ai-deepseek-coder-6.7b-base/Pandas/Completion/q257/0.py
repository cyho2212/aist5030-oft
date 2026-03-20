df['Time'] = df['Time'].dt.floor('2min')
df = df.groupby('Time').mean()
df.reset_index(inplace=True)

print(df)
