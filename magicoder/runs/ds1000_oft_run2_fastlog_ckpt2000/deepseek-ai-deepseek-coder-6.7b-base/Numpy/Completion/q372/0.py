    return (np.cos(x)**4 + np.sin(y)**2)

# Simpson's rule
def simpson_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

print(simpson_rule(f, 0, 1, 20))
