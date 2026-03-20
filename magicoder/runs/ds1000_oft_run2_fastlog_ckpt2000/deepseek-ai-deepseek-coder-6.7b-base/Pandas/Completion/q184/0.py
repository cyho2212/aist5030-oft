df['Date'] = df['Member'].map(dict).fillna('17/8/1926')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.strftime('%d-%b-%Y')
print(df)
