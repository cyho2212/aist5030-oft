result = df.assign(var2=df['var2'].str.split(',')).explode('var2')

print(result)
