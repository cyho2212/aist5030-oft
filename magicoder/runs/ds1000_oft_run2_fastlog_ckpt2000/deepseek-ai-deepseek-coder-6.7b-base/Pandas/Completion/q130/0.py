df['index_original'] = df.duplicated(subset=['col1','col2'], keep='first').cumsum()

print(df)
