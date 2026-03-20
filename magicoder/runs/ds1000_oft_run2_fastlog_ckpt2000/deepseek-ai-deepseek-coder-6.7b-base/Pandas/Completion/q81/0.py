result = pd.concat([df.iloc[-3:].sum(), df.iloc[-2:].mean(), df.iloc[-3:].sum(), df.iloc[-2:].mean()])

print(result)
