    sA = sA.tocsr()
    sA = sA + sA.T - np.diag(sA.diagonal())
    return sA
