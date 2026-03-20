df['datetime'] = df['datetime'].dt.tz_localize(None)
df['datetime'] = df['datetime'].dt.strftime('%d-%b-%Y %H:%M:%S')

print(df)
