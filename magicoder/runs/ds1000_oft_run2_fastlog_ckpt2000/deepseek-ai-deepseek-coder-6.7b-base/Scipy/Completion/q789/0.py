def dN1_dt_simple(t, N1):
    return -100 * N1 + t - np.sin(t) if 0 < t < 2*np.pi else 2*np.pi

sol = scipy.integrate.solve_ivp(fun=dN1_dt_simple, t_span=time_span, y0=[N0,])
result = sol.y
