def multinomial_likelihood(weights, data):
    return np.prod(np.power(weights, data.values))

def multinomial_log_likelihood(weights, data):
    return np.sum(data.values * np.log(weights))

def multinomial_mle(data):
    return sciopt.fmin(lambda w: -multinomial_log_likelihood(w, data), np.ones(data.shape[1]), disp=False)

weights = multinomial_mle(a)
print(weights)
