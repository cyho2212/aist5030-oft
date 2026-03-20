result = np.zeros((5, 100))
for i in range(5):
    tck = interpolate.splrep(x[:, i], y[:, i], k = 2, s = 4)
    result[i] = interpolate.splev(x_val, tck, der = 0)
