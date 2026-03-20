def f(x, y):
    return (np.cos(x))**4 + (np.sin(y))**2

def simpson_2d(f, x, y):
    hx = x[1] - x[0]
    hy = y[1] - y[0]
    nx = len(x)
    ny = len(y)
    s = 0
    for i in range(nx):
        for j in range(ny):
            if i == 0 or i == nx-1 or j == 0 or j == ny-1:
                s += f(x[i], y[j])
            elif i % 2 == 0 and j % 2 == 0:
                s += 2 * f(x[i], y[j])
            elif i % 2 == 1 and j % 2 == 1:
                s += 4 * f(x[i], y[j])
            else:
                s += 12 * f(x[i], y[j])
    return s * (hx * hy / 9.0)

result = simpson_2d(f, x, y)
print(result)
