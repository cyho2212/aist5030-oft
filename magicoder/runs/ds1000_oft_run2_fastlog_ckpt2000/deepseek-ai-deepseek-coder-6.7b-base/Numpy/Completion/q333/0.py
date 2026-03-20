if denominator == 0:
    result = (np.nan, np.nan)
else:
    result = (numerator // denominator, denominator // np.gcd(numerator, denominator))

print(result)
