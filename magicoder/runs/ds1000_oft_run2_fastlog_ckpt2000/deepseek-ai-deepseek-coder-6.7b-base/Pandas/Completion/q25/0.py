df['Date'] = df['Date'].dt.strftime('%d-%b-%Y %A')
df = df[(df['Date'] >= List[0]) & (df['Date'] <= List[1])]
print(df)
