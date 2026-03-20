# Calculate the pooled variance
pooled_var = ((anobs - 1) * avar + (bnobs - 1) * bvar) / (anobs + bnobs - 2)
# Calculate the t-statistic
t_stat = (amean - bmean) / np.sqrt(pooled_var * (1 / anobs + 1 / bnobs))
# Calculate the degrees of freedom
df = anobs + bnobs - 2
# Calculate the p-value
p_value = 2 * (1 - scipy.stats.t.cdf(np.abs(t_stat), df))
print(p_value)
