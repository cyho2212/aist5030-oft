df['cummax'] = df.groupby('id')['val'].cummax()
print(df)
