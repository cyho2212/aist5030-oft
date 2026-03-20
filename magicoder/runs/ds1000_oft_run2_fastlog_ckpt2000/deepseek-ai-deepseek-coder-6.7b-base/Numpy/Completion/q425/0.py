result = np.unpackbits(np.left_shift(a, m-8).astype(np.uint8), axis=1)[:,::-1]
print(result)
