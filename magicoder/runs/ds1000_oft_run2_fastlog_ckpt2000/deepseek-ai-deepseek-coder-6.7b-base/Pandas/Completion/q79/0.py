result = df.rolling(3, min_periods=1).mean().iloc[::-1]

print(result)
