def func(x,a):
    return a.dot(x**2)
def residual(x, a, y):
    return (y - func(x,a)) **2
out = scipy.optimize.minimize(residual, x0, args=(a, y))
print(out)
