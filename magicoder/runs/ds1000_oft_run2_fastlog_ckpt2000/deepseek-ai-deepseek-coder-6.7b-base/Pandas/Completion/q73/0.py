df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')
df = df.sort_values(by='date')
df = df.drop_duplicates(subset='date', keep='first')
df = df.set_index('date')
df = df.drop(df.index[df.index.duplicated(keep='first')])
df = df.reset_index()

print(df)
