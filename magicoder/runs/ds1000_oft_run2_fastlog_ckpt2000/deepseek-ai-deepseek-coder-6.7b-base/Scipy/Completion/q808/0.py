def bekkers_cdf(x, a, m, d):
    return integrate.quad(lambda x: bekkers(x, a, m, d), 0, x)[0]

def bekkers_ppf(p, a, m, d):
    return sp.optimize.fsolve(lambda x: bekkers_cdf(x, a, m, d) - p, 1)[0]

def bekkers_rvs(a, m, d, size=1):
    return np.array([bekkers_ppf(np.random.uniform(), a, m, d) for _ in range(size)])

def bekkers_fit(data, a, m, d):
    return bekkers(data, a, m, d)

def bekkers_test(data, a, m, d):
    return stats.kstest(data, lambda x: bekkers_fit(x, a, m, d))

result = bekkers_test(sample_data, estimated_a, estimated_m, estimated_d)
print(result)
