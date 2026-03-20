    # Calculate the CDF of the uniform distribution
    uniform_cdf = lambda x: x / T
    # Calculate the CDF of the exponential distribution
    exponential_cdf = lambda x: 1 - np.exp(-rate * x)
    # Calculate the CDF of the times
    times_cdf = lambda x: np.sum(np.array(times) < x) / len(times)
    # Calculate the Kolmogorov-Smirnov statistic
    ks_statistic = max(np.abs(uniform_cdf(times) - times_cdf(times)))
    return ks_statistic
print(f())
