df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')
df = df.sort_values(by='date')
df['date_diff'] = df['date'].diff()
df['date_diff'] = df['date_diff'].dt.days
df = df[df['date_diff'] > X]
result = df.reset_index(drop=True)

print(result)
