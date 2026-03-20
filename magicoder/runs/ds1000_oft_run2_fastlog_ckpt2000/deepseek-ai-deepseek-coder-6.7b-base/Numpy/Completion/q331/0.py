result = np.array(np.gcd(numerator, denominator))
result = (numerator // result[0], denominator // result[0])
print(result)
