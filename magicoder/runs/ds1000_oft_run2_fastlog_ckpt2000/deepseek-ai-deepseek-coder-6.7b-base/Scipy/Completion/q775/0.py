result = sparse.diags(matrix, [-1,0,1], (5, 5)).toarray()
print(result)
