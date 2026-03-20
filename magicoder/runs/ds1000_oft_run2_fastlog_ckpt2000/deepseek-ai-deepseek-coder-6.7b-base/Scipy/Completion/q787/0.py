def func(x, a):
    return a.dot(x ** 2)

def residual(x, a, y):
    return (y - func(x, a)) ** 2

def main():
    out = scipy.optimize.minimize(residual, x0, args=(a, y), method='L-BFGS-B', bounds=[(x_lower_bounds[i], None) for i in range(len(x_lower_bounds))])
    print(out)

if __name__ == '__main__':
    main()
