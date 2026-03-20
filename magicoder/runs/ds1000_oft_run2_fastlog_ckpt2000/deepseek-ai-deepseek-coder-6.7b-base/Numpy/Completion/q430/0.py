    mean = np.mean(a)
    std = np.std(a)
    third_std = std * 3
    lower_bound = mean - third_std
    upper_bound = mean + third_std
    return (lower_bound, upper_bound)

print(f())
