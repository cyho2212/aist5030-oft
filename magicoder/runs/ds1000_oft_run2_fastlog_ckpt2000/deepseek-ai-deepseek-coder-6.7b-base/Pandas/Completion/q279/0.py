result = df[(df.index < '2020-02-17 15:30:00') | (df.index > '2020-02-18 21:59:00')]

# Day of the week
result['Day of the week'] = result.index.day_name()

# Format date
result.index = result.index.strftime('%d-%b-%Y %A')

print(result)
