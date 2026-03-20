result = distance.cdist(np.arange(shape[0]*shape[1]).reshape(shape), np.array([shape[0]//2, shape[1]//2]), 'cityblock')
