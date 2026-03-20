M = M + M.T - sparse.diags(M.diagonal())
