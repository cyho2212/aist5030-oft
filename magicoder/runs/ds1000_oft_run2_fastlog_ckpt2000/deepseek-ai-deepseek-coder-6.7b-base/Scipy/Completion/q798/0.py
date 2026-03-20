V = V.tocsr()
V = V + x
V = V.tolil()
V = V + y
V = V.tocsr()
