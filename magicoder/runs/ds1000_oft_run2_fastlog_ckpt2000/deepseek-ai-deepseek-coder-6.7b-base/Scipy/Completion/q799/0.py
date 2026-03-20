sa = sa.tocsc()
for Col in range(sa.shape[1]):
    Column = sa[:,Col].data
    List = [x**2 for x in Column]
    Len = math.sqrt(sum(List))
    sa[:,Col].data = np.array([x/Len for x in Column])
