result = np.roll(a, shift)
if shift > 0:
    result[:shift] = np.nan
else:
    result[shift:] = np.nan
print(result)
