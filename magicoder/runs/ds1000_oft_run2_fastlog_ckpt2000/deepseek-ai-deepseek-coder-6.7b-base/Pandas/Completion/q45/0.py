result = df.apply(lambda x : (x[x.isnull()].values.tolist()+x[x.notnull()].values.tolist()),1)
print(result)
