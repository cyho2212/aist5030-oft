    dev = abs((x-u)/o2)
    P_inner = scipy.integrate.quad(NDfx,-dev,dev)[0]
    P_outer = 1 - P_inner
    P = P_inner + P_outer/2
    return(P)
print(f())
