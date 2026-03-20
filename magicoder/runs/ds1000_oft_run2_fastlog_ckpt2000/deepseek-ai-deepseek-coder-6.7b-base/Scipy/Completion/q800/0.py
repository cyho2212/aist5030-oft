sa = sa.tocsr()
for Col in range(sa.shape[1]):
    column = sa[:,Col].data
    List = [x**2 for x in column]
    Len = math.sqrt(sum(List))
    sa[:,Col].data = np.array([x/Len for x in column])
