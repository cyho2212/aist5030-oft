result = np.array([fsolve(eqn, x0=0.5, args = (a,b)) for a, b in zip(xdata, bdata)])
print(result)
