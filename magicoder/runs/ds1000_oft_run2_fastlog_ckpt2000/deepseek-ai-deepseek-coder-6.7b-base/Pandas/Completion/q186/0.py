df['Date'] = pd.to_datetime(df['Date'], format= '%d/%m/%y')
df['Count_d'] = df.Date.map(df.groupby('Date').size())
df['Count_m'] = df.Date.map(df.groupby(df['Date'].dt.to_period('M')).size())
df['Count_y'] = df.Date.map(df.groupby(df['Date'].dt.to_period('Y')).size())
df['Count_Val'] = df.groupby(['Date', 'Val']).size()

print(df)
