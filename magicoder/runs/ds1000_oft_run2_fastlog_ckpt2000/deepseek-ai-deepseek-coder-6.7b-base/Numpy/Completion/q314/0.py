result = np.unravel_index(np.argsort(a.ravel())[-2], a.shape)
print(result)
