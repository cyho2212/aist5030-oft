df.columns = ['X' + col if col != 'HeaderX' else col for col in df.columns]

print(df)
