
# Calculate the mean and standard deviation
mean = np.mean(a)
std = np.std(a)

# Calculate the 2nd standard deviation
two_std = std * 2

# Calculate the 2nd standard deviation interval
lower_bound = mean - two_std
upper_bound = mean + two_std

# Create a boolean array indicating whether each value is an outlier
result = np.logical_or(a < lower_bound, a > upper_bound)

print(result)
