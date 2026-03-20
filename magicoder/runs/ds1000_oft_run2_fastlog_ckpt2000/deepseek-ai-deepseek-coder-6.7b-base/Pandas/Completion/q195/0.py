result = df.var2.str.split(',', expand=True).stack().reset_index(level=1, drop=True).to_frame('var2').join(df.var1).reset_index(drop=True)

print(result)
