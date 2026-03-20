df['arrival_time'] = pd.to_datetime(df['arrival_time'])
df['departure_time'] = pd.to_datetime(df['departure_time'])
df['Duration'] = df['departure_time'] - df['arrival_time']
df['Duration'] = df['Duration'].dt.total_seconds()
df['arrival_time'] = df['arrival_time'].dt.strftime('%d-%b-%Y %H:%M:%S')
df['departure_time'] = df['departure_time'].dt.strftime('%d-%b-%Y %H:%M:%S')
print(df)
