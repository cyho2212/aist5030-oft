df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
df['Count_d'] = df.groupby('Date').size()
df['Count_m'] = df.groupby([df['Date'].dt.year, df['Date'].dt.month]).size()
df['Count_y'] = df.groupby(df['Date'].dt.year).size()
df['Count_w'] = df.groupby(df['Date'].dt.weekday).size()
df['Count_Val'] = df.groupby(['Date', 'Val']).size()

print(df)
