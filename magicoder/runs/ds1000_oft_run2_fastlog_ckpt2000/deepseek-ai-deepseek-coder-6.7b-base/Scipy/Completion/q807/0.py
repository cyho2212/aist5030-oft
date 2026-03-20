result = []
for x, a in zip(xdata, adata):
    b = fsolve(lambda b: eqn(x, a, b), x0=0.5)
    result.append(b)
