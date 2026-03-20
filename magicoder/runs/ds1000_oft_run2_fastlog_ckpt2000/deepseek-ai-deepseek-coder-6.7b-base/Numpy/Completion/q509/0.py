result = im[np.any(im, axis=1)][:, np.any(im, axis=0)]
print(result)
