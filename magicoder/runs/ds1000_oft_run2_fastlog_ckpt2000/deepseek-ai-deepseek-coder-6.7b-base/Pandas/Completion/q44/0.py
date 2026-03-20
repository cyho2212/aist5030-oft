result = df.apply(lambda x : (x[x.notnull()].values.tolist()+x[x.isnull()].values.tolist()),1)
print(result)
