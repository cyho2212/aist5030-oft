def func(x, a, b, c):
    return a*np.exp(b*x) + c

result = scipy.optimize.curve_fit(func, x, y, p0)
print(result[0])
