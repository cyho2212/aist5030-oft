cols = df.columns[2:4]
df[cols + '_scale'] = df.groupby('Month')[cols].apply(lambda x: scaler.fit_transform(x))
print(df)
