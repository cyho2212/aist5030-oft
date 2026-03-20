df['Time'] = pd.to_datetime(df['Time'])
df = df.set_index('Time')
df['A_integral'] = df['A'].rolling(window=2).apply(lambda x: integrate.trapz(x, dx=1))
print(df)
