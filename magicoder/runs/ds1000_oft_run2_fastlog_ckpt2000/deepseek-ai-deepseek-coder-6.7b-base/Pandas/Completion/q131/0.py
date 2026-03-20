df['index_original'] = df.groupby(['col1', 'col2']).cumcount()
print(df)
